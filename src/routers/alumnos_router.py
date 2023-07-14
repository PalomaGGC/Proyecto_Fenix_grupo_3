from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError
from services.alumnos_services import Alumnos_services
from config.db import Base, Session, engine




alumnos = APIRouter(tags=["alumnos"])


# @alumnos.on_event("startup")
# def startup():
#     # create db tables
#     with engine.begin() as conn:
#         conn.run(Base.metadata.drop_all)
#         conn.run(Base.metadata.create_all)


#COSULTAR
@alumnos.get("/alumnos", response_model=List[Alumnos], status_code=200)
def todosLosAlumnos() -> List[Alumnos]:
    db = Session()
    result = Alumnos_services(db).consultar_alumnos()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# #CONSULTAR SOLO UNO
# @alumnos.get("/alumnos/{nie}")
# def obtenerAlumnoPorNIE(nie: int):
#     alumno = Alumnos_services()
#     result = alumno.alumno(nie)
#     return result



@alumnos.post("/alumnos", response_model=dict, status_code=201)
def agregarAlumno(alumno: Alumnos) -> dict:
    db = Session()
    Alumnos_services(db).agregar_alumno(alumno)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo alumno"})


# #EDITAR
# @alumnos.put("/alumnos/{alumno_id}")
# def editarAlumno(alumno_id: int, alumno: Alumnos):
#     alumnos = Alumnos_services()
#     result = alumnos.editar_alumno(alumno_id, alumno)
#     return result


