from typing import List
from fastapi import APIRouter, Depends
from schemas.profesores import Profesores
from services.profesores_services import Profesores_services
from config.db import Base, engine
from middlewares.jwt_bearer import JWTBearer


profesores = APIRouter(tags=["profesores"])

#CREAR LAS TABLAS
@profesores.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# COSULTAR TODOS LOS PROFESORES
@profesores.get("/profesores", response_model=List[Profesores])
def consultar_profesores() -> List[Profesores]:
    result = Profesores_services().consultar_profesores()
    return result


# CONSULTAR PROFESOR POR NOMBRE
@profesores.get('/profesor/{nombre}', response_model=Profesores)# nombre es el parámetro de ruta que espero recibir cuando el usuario acceda  a esta url
def consultar_profesor_por_nombre(nombre:str) -> Profesores:
    #Creo una sesión para conectarme a la base de datos, la variable db será una instancia de session, que ya importé al inicio
    result = Profesores_services().consultar_profesor(nombre)
    #De Profesores_services primero obtengo la sesión y luego le paso el método consultar_profesor
    #Consulto los datos de ProfesorModel y hago un filtrado por nombre, le digo que obtenga el primer resultado.
    return result


# AÑADIR UN NUEVO PROFESOR A LA TABLA
@profesores.post("/profesores", response_model=dict, dependencies=[Depends(JWTBearer())]) #dependencies=[Depends(JWTBearer())]
def agregar_profesor(profesor: Profesores) -> dict:
    result = Profesores_services().agregar_profesor(profesor)
    return result


# MODIFICAR LOS DATOS DE UN PROFESOR
@profesores.put('/profesores/{nombre}', response_model=dict, dependencies=[Depends(JWTBearer())])
def editar_profesor(nombre: str, data:Profesores) -> dict:
    result = Profesores_services().editar_profesor(nombre, data)
    return result


# BORRAR UN PROFESOR
@profesores.delete('/profesores/{nombre}', response_model=dict, dependencies=[Depends(JWTBearer())])
def borrar_profesor(nombre: str) -> dict:
    result = Profesores_services().borrar_profesor(nombre)
    return result
