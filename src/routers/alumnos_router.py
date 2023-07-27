from typing import List
from fastapi import APIRouter, Depends
from fastapi.testclient import TestClient
from middlewares.jwt_bearer import JWTBearer
from schemas.alumnos import Alumnos
from services.alumnos_services import Alumnos_services
from config.db import Base, engine


alumnos = APIRouter(tags=["alumnos"])

# CREAR TABLAS DE ALUMNOS
@alumnos.on_event("startup")
def startup():
    # create db table
    Base.metadata.create_all(bind=engine)


# COSULTAR TODOS LOS ALUMNOS
@alumnos.get("/alumnos", response_model=List[Alumnos])
def consultar_alumnos() -> List[Alumnos]:
    result = Alumnos_services().consultar_alumnos()
    return result


# CONSULTAR ALUMNO POR ID
@alumnos.get('/alumno/{id}', response_model=Alumnos)# id es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
def consultar_alumno_por_id(id:str) -> Alumnos:
    result = Alumnos_services().consultar_alumno(id)
    return result


# AGREGAR UN NUEVO ALUMNO
@alumnos.post("/alumnos", response_model=dict)
def agregar_alumno(alumno: Alumnos) -> dict:
    result = Alumnos_services().agregar_alumno(alumno)
    return result



# Corrección del decorador
@alumnos.put('/alumnos/{id}', response_model=dict)
def editar_alumno(id: str, data: Alumnos) -> dict:
    result = Alumnos_services().editar_alumno(id, data)
    return result



# BORRAR UN ALUMNO
@alumnos.delete('/alumnos/{id}', response_model=dict)
def borrar_alumno(id: str) -> dict:
    result = Alumnos_services().borrar_alumno(id)
    return result

