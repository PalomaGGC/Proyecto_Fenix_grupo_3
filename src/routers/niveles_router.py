from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.niveles import Niveles
from sqlalchemy.exc import SQLAlchemyError
from services.niveles_services import Niveles_services
from config.db import Base, Session, engine
from models.nivelesModel import Niveles_model


niveles = APIRouter(tags=["niveles"])

#CREAR LAS TABLAS
@niveles.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


#COSULTAR
@niveles.get("/niveles", response_model=List[Niveles], status_code=200)
def consultar_niveles() -> List[Niveles]:
    result = Niveles_services().consultar_niveles()

    if not result:
        return None

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@niveles.get('/nivel/{nombre}', response_model=Niveles)# nombre es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
def consultar_nivel_por_nombre(nombre:str) -> Niveles:
    #Creo una sesión para conectarme a la base de datos, la variable db será una instancia de session, que ya importé al inicio
    result = Niveles_services().consultar_nivel(nombre)
    #De Niveles_services primero obtengo la sesión y luego le paso el método consultar_nivel
    #Consulto los datos de Niveles_model y hago un filtrado por nombre, le digo que obtenga el primer resultado.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@niveles.post("/niveles", response_model=dict, status_code=201)
def agregar_nivel(nivel: Niveles) -> dict:
    Niveles_services().agregar_nivel(nivel)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo nivel"})



@niveles.put('/niveles/{nombre}', response_model=dict, status_code=200)
def editar_nivel(nombre: str, data:Niveles) -> dict:
    result = Niveles_services().consultar_nivel(nombre)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})

    Niveles_services().editar_nivel(nombre, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el nivel"})





































