from models.incripcionesModel import Inscripciones_model
from dateutil.relativedelta import relativedelta
from config.db import Session
from sqlalchemy import func
import datetime
import sched
import time
from logger import Logs


logger= Logs()

def ejecutar_funcion_en_hora_especifica(hora, minuto, segundos):
    # Crea un objeto scheduler
    programador = sched.scheduler(time.time, time.sleep)

    # Obtiene la hora actual
    ahora = time.localtime()
    # Establece la hora específica del día para la ejecución
    hora_especifica = time.struct_time((ahora.tm_year, ahora.tm_mon, ahora.tm_mday, hora, minuto, segundos, ahora.tm_wday, ahora.tm_yday, ahora.tm_isdst))

    # Calcula la cantidad de segundos entre la hora actual y la hora específica
    tiempo_espera = time.mktime(hora_especifica) - time.mktime(ahora)

    # Programa la ejecución de la función en la hora específica
    programador.enter(tiempo_espera, 1, crear_nueva_inscripcion, ())

    # Ejecuta el scheduler
    programador.run()


# CREAR UNA NUEVA INSCRIPCIÓN
def crear_nueva_inscripcion():
    try:
        db = Session()
        # Obtener la fecha actual sin la hora
        fecha_actual = datetime.datetime.now().date()
        print("Fecha actual:", fecha_actual)

        # Filtrar las inscripciones donde la fecha de finalización (sin la hora) sea menor o igual a la fecha actual
        inscripciones = db.query(Inscripciones_model).filter(func.DATE(Inscripciones_model.fecha_fin) == fecha_actual).all()
        print("Número de inscripciones encontradas:", len(inscripciones))

        nuevas_inscripciones = []  # Lista para almacenar las nuevas inscripciones

        for inscripcion in inscripciones:
            # Calcular la nueva fecha de inicio y fin para el próximo mes
            fecha_fin_mes_actual = inscripcion.fecha_fin
            nueva_fecha_inicio = fecha_fin_mes_actual + datetime.timedelta(days=1)
            nueva_fecha_fin = nueva_fecha_inicio + relativedelta(months=1) - datetime.timedelta(days=1)

            # Crear una nueva inscripción con los datos actualizados y agregarla a la lista
            nueva_inscripcion = Inscripciones_model(
                profesor_clase_id=inscripcion.profesor_clase_id,
                alumno_id=inscripcion.alumno_id,
                precio_clase=inscripcion.precio_clase,
                descuento_inscripcion=inscripcion.descuento_inscripcion,
                descuento_familiar=inscripcion.descuento_familiar,
                precio_con_descuento=inscripcion.precio_con_descuento,
                pagada="false",
                fecha_inscripcion=nueva_fecha_inicio,
                fecha_fin=nueva_fecha_fin
            )
            nuevas_inscripciones.append(nueva_inscripcion)

        # Agregar todas las nuevas inscripciones a la sesión y confirmar los cambios en la base de datos
        db.add_all(nuevas_inscripciones)
        db.commit()
        print("Nuevas inscripciones creadas:", len(nuevas_inscripciones))

    except Exception as e:
        # print(f"Error al crear las nuevas inscripciones: {e}")
        logger.error("Error al crear las nuevas inscripciones automaticas: %s", e)


    finally:
        db.close()

