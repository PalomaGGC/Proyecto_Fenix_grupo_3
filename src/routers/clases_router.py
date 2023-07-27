from typing import List
from fastapi import APIRouter, Depends
from middlewares.jwt_bearer import JWTBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from services.clases_services import Clases_services
from schemas.clases import Clases
from config.db import Base, engine


clases = APIRouter(tags=["clases"])


@clases.on_event("startup")
def startup():
     # create db tables
    Base.metadata.create_all(bind=engine)


# CONSULTAR CLASES
@clases.get('/clases', response_model= List[Clases] )
def consultar_clases() -> List[Clases]:
    result = Clases_services().consultar_clases()
    return result


# CONSULTAR UNA CLASE POR ID
@clases.get('/clase/{id}', response_model= Clases)
def consultar_clase_por_id(id: int) -> Clases:
    result = Clases_services().consultar_clase_por_id(id)
    return result


# AGREGAR UNA NUEVA CLASE
@clases.post("/clases", response_model=dict, dependencies=[Depends(JWTBearer())])
def agregar_clase(clase: Clases)-> dict:
    result = Clases_services().agregar_clase(clase)
    return result


# EDITAR UNA CLASE
@clases.put("/clases/{id}", response_model=dict, dependencies=[Depends(JWTBearer())])
def editar_clase(id: int, data: Clases)-> dict:
    result = Clases_services().editar_clase(id, data)
    return result




@clases.delete('/clase/{id}', response_model=dict)
def borrar_clase(id: int) -> dict:
    result = Clases_services().borrar_clase(id)
    return result
