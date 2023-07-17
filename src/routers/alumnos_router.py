from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError
from services.alumnos_services import Alumnos_services
from config.db import Base, Session, engine
from models.alumnosModel import Alumnos_model


alumnos = APIRouter(tags=["alumnos"])

#CREAR LAS TABLAS
@alumnos.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


#COSULTAR
@alumnos.get("/alumnos", response_model=List[Alumnos], status_code=200)
def consultar_alumnos() -> List[Alumnos]:
    result = Alumnos_services().consultar_alumnos()

    if not result:
        return None

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alumnos.get('/alumno/{nie}', response_model=Alumnos)# nie es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
def consultar_alumno_por_nie(nie:str) -> Alumnos:
    #Creo una sesión para conectarme a la base de datos, la variable db será una instancia de session, que ya importé al inicio
    result = Alumnos_services().consultar_alumno(nie)
    #De Alumnos_services primero obtengo la sesión y luego le paso el método consultar_alumno
    #Consulto los datos de Alumnos_model y hago un filtrado por nie, le digo que obtenga el primer resultado.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alumnos.post("/alumnos", response_model=dict, status_code=201)
def agregar_alumno(alumno: Alumnos) -> dict:
    Alumnos_services().agregar_alumno(alumno)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo alumno"})



@alumnos.put('/alumnos/{nie}', response_model=dict, status_code=200)
def editar_alumno(nie: str, data:Alumnos) -> dict:
    result = Alumnos_services().consultar_alumno(nie)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})

    Alumnos_services().editar_alumno(nie, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el alumno"})


@alumnos.delete('/alumnos/{nie}', response_model=dict, status_code=200)
def borrar_alumno(nie: str) -> dict:
    result = Alumnos_services().consultar_alumno(nie)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    Alumnos_services().borrar_alumno(nie)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el alumno"})


