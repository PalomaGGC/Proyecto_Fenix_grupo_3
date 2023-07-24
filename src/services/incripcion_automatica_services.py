from models.incripcionesModel import Inscripciones_model
from dateutil.relativedelta import relativedelta
from config.db import Base, engine, Session
from sqlalchemy import DateTime, func
import schedule
import datetime


# Esta funcion realiza el proceso de obtener las inscripciones cuya fecha de fin es igual a la fecha actual,
# luego itera sobre cada inscripción para crear una nueva inscripción con los datos actualizados y, 
# finalmente, agrega la nueva inscripción a la base de datos. Este proceso se programa para ejecutarse
# diariamente a la medianoche utilizando la librería schedule. "Esta funcion se llama en app.py"
def crear_nueva_inscripcion():
    try:
        db = Session()
        # Obtener la fecha actual sin la hora
        fecha_actual = datetime.datetime.now().date()

        # Filtrar las inscripciones donde la fecha de finalización (sin la hora) sea menor o igual a la fecha actual
        inscripciones = db.query(Inscripciones_model).filter(func.DATE(Inscripciones_model.fecha_fin) == fecha_actual).all()
        # inscripciones = db.query(Inscripciones_model).filter(Inscripciones_model.fecha_fin <= func.current_date()).all()
        for inscripcion in inscripciones:
            # Calcular la nueva fecha de inicio y fin para el próximo mes
            fecha_fin_mes_actual = inscripcion.fecha_fin
            nueva_fecha_inicio = fecha_fin_mes_actual + datetime.timedelta(days=1)
            nueva_fecha_fin = nueva_fecha_inicio + relativedelta(months=1) - datetime.timedelta(days=1)

            # Crear una nueva inscripción con los datos actualizados
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

            db.add(nueva_inscripcion)  # Agregar la nueva inscripción a la sesión
            db.commit()  # Confirmar los cambios en la base de datos
        
        # return "todo ok"
        db.close()

    except Exception as e:
        print(f"Error al crear la nueva inscripción: {e}")

# Programo la ejecución de la función cada día a la medianoche
schedule.every().day.at("17:48:00").do(crear_nueva_inscripcion)

