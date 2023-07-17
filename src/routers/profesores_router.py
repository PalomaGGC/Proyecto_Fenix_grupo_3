from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.profesoresModel import Profesores_model
from schemas.profesores import Profesores
from sqlalchemy.exc import SQLAlchemyError
from services.profesores_services import Profesores_services
from config.db import Base, Session, engine


profesores = APIRouter(tags=["profesores"])

#CREAR LAS TABLAS
@profesores.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# COSULTAR TODOS LOS PROFESORES
@profesores.get("/profesores", response_model=List[Profesores], status_code=200)
def consultar_profesores() -> List[Profesores]:
    db = Session()
    result = Profesores_services(db).consultar_profesores()

    if not result:
        return None

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# CONSULTAR PROFESOR POR NOMBRE
@profesores.get('/profesor/{nombre}', response_model=Profesores)# nombre es el parámetro de ruta que espero recibir cuando el usuario acceda  a esta url
def consultar_profesor_por_nombre(nombre:str) -> Profesores:
    db = Session()
    #Creo una sesión para conectarme a la base de datos, la variable db será una instancia de session, que ya importé al inicio
    result = Profesores_services(db).consultar_profesor(nombre)
    #De Profesores_services primero obtengo la sesión y luego le paso el método consultar_profesor
    #Consulto los datos de ProfesorModel y hago un filtrado por nombre, le digo que obtenga el primer resultado.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# AÑADO UN NUEVO PROFESOR A LA TABLA
@profesores.post("/profesores", response_model=dict, status_code=201)
def agregar_profesor(profesor: Profesores) -> dict:
    db = Session()
    Profesores_services(db).agregar_profesor(profesor)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo profesor"})


# MODIFICO LOS DATOS DE UN PROFESOR
@profesores.put('/profesores/{nombre}', response_model=dict, status_code=200)
def editar_profesor(nombre: str, data:Profesores) -> dict:
    db = Session()
    result = Profesores_services(db).consultar_profesor(nombre)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})

    Profesores_services(db).editar_profesor(nombre, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el profesor"})

# BORRO UN PROFESOR
@profesores.delete('/profesores/{nombre}', response_model=dict, status_code=200)
def borrar_profesor(nombre: str) -> dict:

    result= db.query(Profesores_model).filter(Profesores_model.nombre_profesor == nombre).first()
    print(result)
    #Realizo la búsqueda del profesor
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    Profesores_services(db).borrar_profesor(nombre)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el profesor"})
