import json
from fastapi import APIRouter
from config.db import conexion
from models.alumnosModel import tabla_alumnos
from schemas.alumnos import Alumnos


alumnos = APIRouter()


@alumnos.get("/alumnos" , tags=["alumnos"])
def todosLosAlumnos():
   # Extraer todos los registros de la tabla "alumnos"
    query = tabla_alumnos.select()
    result = conexion.execute(query).fetchall()

    alumnos=[]
    
    #recorro los datos y lo agrego al alumnos = []
    for item in result:
        alumno = {
            "nomnbre_alumno":item[1],
            "apellido_añumno":item[2],
            "edad_alumno":item[3],
            "nie_alumno":item[4],
            "telefono_alumno":item[5],
            "email_alumno":item[6],
            "descuento_familiar":item[7]
        }
        
        alumnos.append(alumno)
  
    return alumnos





@alumnos.post("/alumnos", tags=["alumnos_agregar"])
def agregarAlumno(alumnos: Alumnos):
    # Verificar si el NIE del alumno ya existe en la base de datos
    existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.nie_alumno == alumnos.nie_alumno)).first()
    if existe_alumno:
        return "No se puede agregar el alumno. El NIE ya está registrado."
    
    #paso los datos a un diccionario
    nuevo_alumno = {
        "nombre_alumno": alumnos.apellido_alumno,
        "apellido_alumno": alumnos.apellido_alumno,
        "edad_alumno": alumnos.edad_alumno,
        "nie_alumno": alumnos.nie_alumno,
        "email_alumno": alumnos.email_alumno,
        "telefono_alumno": alumnos.telefono_alumno,
        "descuento_familiar": alumnos.descuento_familiar
    }
    
    #me conecto a la base de datos y preparo los valores que se van a guardar
    conexion.execute(tabla_alumnos.insert().values(nuevo_alumno))
    #hago un commit a la base de datos, envio los datos a la base de datos
    conexion.commit()
    
    return f"Se agregó el alumno {nuevo_alumno} correctamente"
