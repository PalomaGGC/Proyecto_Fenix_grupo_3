from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError
from services.alumnos_services import Alumnos_services
from config.db import Base, Session, engine
from models.alumnosModel import Alumnos_model

alumnos = APIRouter(tags=["alumnos"])

# CREAR TABLAS
@alumnos.on_event("startup")
def startup():
    # create db table
    Base.metadata.create_all(bind=engine)
    

#COSULTAR
@alumnos.get("/alumnos", response_model=List[Alumnos], status_code=200)
def consultar_alumnos() -> List[Alumnos]:
    result = Alumnos_services().consultar_alumnos()

    if not result:
        return None
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alumnos.get('/alumno/{id}', response_model=Alumnos)# id es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
def consultar_alumno_por_id(id:str) -> Alumnos:
    result = Alumnos_services().consultar_alumno(id)
    #Consulto los datos de Alumnos_model y hago un filtrado por id, le digo que obtenga el primer resultado.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alumnos.post("/alumnos", response_model=dict, status_code=201)
def agregar_alumno(alumno: Alumnos) -> dict:
    Alumnos_services().agregar_alumno(alumno)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo alumno"})



@alumnos.put('/alumnos/{id}', response_model=dict, status_code=200)
def editar_alumno(id: str, data:Alumnos) -> dict:
    result = Alumnos_services().consultar_alumno(id)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})

    Alumnos_services().editar_alumno(id, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el alumno"})


@alumnos.delete('/alumnos/{id}', response_model=dict, status_code=200)
def borrar_alumno(id: str) -> dict:
    result =Alumnos_services().consultar_alumno(id)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    Alumnos_services().borrar_alumno(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el alumno"})

