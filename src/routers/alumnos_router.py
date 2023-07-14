from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError
from services.alumnos_services import Alumnos_services
from config.db import Session



alumnos = APIRouter(tags=["alumnos"])

#COSULTAR
@alumnos.get("/alumnos")
def todosLosAlumnos():
    alumnos = Alumnos_services()
    result = alumnos.alumnos()
    return result



#CONSULTAR SOLO UNO
@alumnos.get("/alumnos/{nie}")
def obtenerAlumnoPorNIE(nie: int):
    alumno = Alumnos_services()
    result = alumno.alumno(nie)
    return result



@alumnos.post("/alumnos", response_model=dict, status_code=201)
def agregarAlumno(alumno: Alumnos) -> dict:
    db = Session()
    Alumnos_services(db).agregar_alumno(alumno)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo alumno"})


#EDITAR
@alumnos.put("/alumnos/{alumno_id}")
def editarAlumno(alumno_id: int, alumno: Alumnos):
    alumnos = Alumnos_services()
    result = alumnos.editar_alumno(alumno_id, alumno)
    return result


