from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from schemas.niveles import Niveles
from services.niveles_services import Niveles_services
from config.db import Base, engine


niveles = APIRouter(tags=["niveles"])

# CREAR LAS TABLAS
@niveles.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# COSULTAR TODOS LOS NIVELES
@niveles.get("/niveles", response_model=List[Niveles])
def consultar_niveles() -> List[Niveles]:
    result = Niveles_services().consultar_niveles()
    return result


# CONSULTAR UN NIVEL POR EL NOMBRE
@niveles.get('/nivel/{nombre}', response_model=Niveles)# nombre es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
def consultar_nivel_por_nombre(nombre:str) -> Niveles:
    result = Niveles_services().consultar_nivel(nombre)
    return result


# AGREGAR UN NUEVO NIVEL
@niveles.post("/niveles", response_model=dict, dependencies=[Depends(JWTBearer())])
def agregar_nivel(nivel: Niveles) -> dict:
    result = Niveles_services().agregar_nivel(nivel)
    return result


# EDITAR UN NIVEL
@niveles.put('/niveles/{nombre}', response_model=dict, dependencies=[Depends(JWTBearer())])
def editar_nivel(nombre: str, data:Niveles) -> dict:
    result = Niveles_services().editar_nivel(nombre, data)
    return result





































