import json
from fastapi import APIRouter
from config.db import conexion
from models.nivelesModel import tabla_niveles
from schemas.niveles import Niveles
from sqlalchemy.exc import SQLAlchemyError

niveles = APIRouter( prefix="/niveles",
                     tags=["niveles"]
                   )

# #COSULTAR
# @niveles.get("/niveles")
# def todosLosNiveles():
#     try:
#         # Extraer todos los registros de la tabla "niveles"
#         query = tabla_niveles.select()
#         result = conexion.execute(query).fetchall()

#         # Convertir los resultados a una lista de niveles
#         niveles = []
#         for item in result:
#             nivel = {
#                 "nombre_nivel": item[1]
#             }
#             niveles.append(nivel)

#         # Retornar la lista de alumnos en formato JSON
#         return niveles
#     except SQLAlchemyError as e:
#         return {"error": str(e)}








# #CONSULTAR SOLO UNO
# @niveles.get("/niveles/{nombre}")
# def obtenerNivelPornombre(nombre: str):
#     try:
#         # Buscar el nivel por su nombre en la base de datos
#         query = tabla_niveles.select().where(tabla_niveles.c.nombre_nivel == nombre)
#         result = conexion.execute(query).fetchone()

#         # Verificar si se encontró un alumno con el nombre especificado
#         if result is None:
#             return {"error": "No se encontró ningún nivel con el nombre especificado."}

#         # Crear un diccionario con los datos del nivel
#         nivel = {
#             "nombre_nivel": result[1]
#         }

#         # Retornar el  en formato JSON
#         return nivel
#     except SQLAlchemyError as e:
#         return {"error": str(e)}






# #AGREGAR
# @niveles.post("/niveles", )
# def agregarNivel(nivel: Niveles):
#     try:
#         # Verificar si el nombre del nivel ya existe en la base de datos
#         existe_nivel = conexion.execute(tabla_niveles.select().where(tabla_niveles.c.nombre_nivel == nivel.nombre_nivel)).first()
#         if existe_nivel:
#             return "No se puede agregar el nivel. El nombre ya está registrado."

#         # Preparar los valores que se van a guardar
#         nuevo_alumno = {
#             "nombre_nivel": nivel.nombre_nivel
#         }

#         # Insertar el nuevo nivel en la base de datos
#         conexion.execute(tabla_niveles.insert().values(**nuevo_alumno))
#         # Hacer un commit a la base de datos
#         conexion.commit()

#         return f"Se agregó el alumno {nuevo_alumno} correctamente"
#     except SQLAlchemyError as e:
#         return {"error": str(e)}
    
    
    
    
    


# #EDITAR
# @alumnos.put("/alumnos/{alumno_id}")
# def editarAlumno(alumno_id: int, alumno: Alumnos):
#     try:
#         # Verificar si el alumno existe en la base de datos
#         existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.id_alumnos == alumno_id)).first()
#         if not existe_alumno:
#             return {"error": "No se encontró ningún alumno con el ID especificado."}

#         # Preparar los valores que se van a actualizar
#         valores_actualizados = {
#             "nombre_alumno": alumno.nombre_alumno,
#             "apellido_alumno": alumno.apellido_alumno,
#             "edad_alumno": alumno.edad_alumno,
#             "nie_alumno": alumno.nie_alumno,
#             "telefono_alumno": alumno.telefono_alumno,
#             "email_alumno": alumno.email_alumno,
#             "descuento_familiar": alumno.descuento_familiar
#         }
        
#         print(valores_actualizados)

#         # Actualizar el alumno en la base de datos
#         query = tabla_alumnos.update().where(tabla_alumnos.c.id_alumnos == alumno_id).values(**valores_actualizados)
#         conexion.execute(query)
#         conexion.commit()

#         return {"message": "Alumno actualizado correctamente."}
#     except SQLAlchemyError as e:
#         return {"error": str(e)}

