from fastapi import APIRouter
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError
from services.alumnos_services import Alumnos_services




alumnos = APIRouter(tags=["alumnos"])

#COSULTAR
@alumnos.get("/alumnos")
async def todosLosAlumnos():
    alumnos = Alumnos_services()
    result = alumnos.alumnos()
    return result



#CONSULTAR SOLO UNO
@alumnos.get("/alumnos/{nie}")
async def obtenerAlumnoPorNIE(nie: int):
    alumno = Alumnos_services()
    result = alumno.alumno(nie)
    return result



#AGREGAR
@alumnos.post("/alumnos")
async def agregar_alumno(alumno: Alumnos):
    alumnos = Alumnos_services()
    result = alumnos.agregar_alumno(alumno)
    return result
    
    

#EDITAR
@alumnos.put("/alumnos/{alumno_id}")
async def editarAlumno(alumno_id: int, alumno: Alumnos):
    alumnos = Alumnos_services()
    result = alumnos.editar_alumno(alumno_id, alumno)
    return result
   

