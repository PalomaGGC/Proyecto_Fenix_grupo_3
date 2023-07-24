from models.incripcionesModel import Inscripciones_model
from dateutil.relativedelta import relativedelta
from config.db import Session, engine
from sqlalchemy import func
import datetime

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
        print(f"Error al crear las nuevas inscripciones: {e}")

    finally:
        db.close()

