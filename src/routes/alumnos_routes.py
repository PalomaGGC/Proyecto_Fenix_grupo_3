import json
from fastapi import APIRouter
from config.db import conexion
from models.alumnosModel import tabla_alumnos
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError

alumnos = APIRouter()

#COSULTAR
@alumnos.get("/alumnos", tags=["alumnos"])
def todosLosAlumnos():
    try:
        # Extraer todos los registros de la tabla "alumnos"
        query = tabla_alumnos.select()
        result = conexion.execute(query).fetchall()

        # Convertir los resultados a una lista de alumnos
        alumnos = []
        for item in result:
            alumno = {
                "nombre_alumno": item[1],
                "apellido_alumno": item[2],
                "edad_alumno": item[3],
                "nie_alumno": item[4],
                "telefono_alumno": item[5],
                "email_alumno": item[6],
                "descuento_familiar": item[7]
            }
            alumnos.append(alumno)

        # Retornar la lista de alumnos en formato JSON
        return alumnos
    except SQLAlchemyError as e:
        return {"error": str(e)}








#CONSULTAR SOLO UNO
@alumnos.get("/alumnos/{nie}", tags=["alumnos"])
def obtenerAlumnoPorNIE(nie: int):
    try:
        # Buscar el alumno por su NIE en la base de datos
        query = tabla_alumnos.select().where(tabla_alumnos.c.nie_alumno == nie)
        result = conexion.execute(query).fetchone()

        # Verificar si se encontró un alumno con el NIE especificado
        if result is None:
            return {"error": "No se encontró ningún alumno con el NIE especificado."}

        # Crear un diccionario con los datos del alumno
        alumno = {
            "nombre_alumno": result[1],
            "apellido_alumno": result[2],
            "edad_alumno": result[3],
            "nie_alumno": result[4],
            "telefono_alumno": result[5],
            "email_alumno": result[6],
            "descuento_familiar": result[7]
        }

        # Retornar el alumno en formato JSON
        return alumno
    except SQLAlchemyError as e:
        return {"error": str(e)}






#AGREGAR
@alumnos.post("/alumnos", tags=["alumnos_agregar"])
def agregarAlumno(alumno: Alumnos):
    try:
        # Verificar si el NIE del alumno ya existe en la base de datos
        existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.nie_alumno == alumno.nie_alumno)).first()
        if existe_alumno:
            return "No se puede agregar el alumno. El NIE ya está registrado."

        # Preparar los valores que se van a guardar
        nuevo_alumno = {
            "nombre_alumno": alumno.nombre_alumno,
            "apellido_alumno": alumno.apellido_alumno,
            "edad_alumno": alumno.edad_alumno,
            "nie_alumno": alumno.nie_alumno,
            "email_alumno": alumno.email_alumno,
            "telefono_alumno": alumno.telefono_alumno,
            "descuento_familiar": alumno.descuento_familiar
        }

        # Insertar el nuevo alumno en la base de datos
        conexion.execute(tabla_alumnos.insert().values(**nuevo_alumno))
        # Hacer un commit a la base de datos
        conexion.commit()

        return f"Se agregó el alumno {nuevo_alumno} correctamente"
    except SQLAlchemyError as e:
        return {"error": str(e)}
    
    
    
    
    


#EDITAR
@alumnos.put("/alumnos/{alumno_id}", tags=["alumnos"])
def editarAlumno(alumno_id: int, alumno: Alumnos):
    try:
        # Verificar si el alumno existe en la base de datos
        existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.id_alumnos == alumno_id)).first()
        if not existe_alumno:
            return {"error": "No se encontró ningún alumno con el ID especificado."}

        # Preparar los valores que se van a actualizar
        valores_actualizados = {
            "nombre_alumno": alumno.nombre_alumno,
            "apellido_alumno": alumno.apellido_alumno,
            "edad_alumno": alumno.edad_alumno,
            "nie_alumno": alumno.nie_alumno,
            "telefono_alumno": alumno.telefono_alumno,
            "email_alumno": alumno.email_alumno,
            "descuento_familiar": alumno.descuento_familiar
        }
        
        print(valores_actualizados)

        # Actualizar el alumno en la base de datos
        query = tabla_alumnos.update().where(tabla_alumnos.c.id_alumnos == alumno_id).values(**valores_actualizados)
        conexion.execute(query)
        conexion.commit()

        return {"message": "Alumno actualizado correctamente."}
    except SQLAlchemyError as e:
        return {"error": str(e)}

