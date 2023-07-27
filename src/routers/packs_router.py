from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from schemas.packs import Packs
from config.db import Base, engine
from services.packs_services import Packs_services

packs = APIRouter(tags=["packs"])

@packs.on_event("startup")
def startup():
   # create db table
    Base.metadata.create_all(bind=engine)


# COSULTAR TODOS LOS PACKS
@packs.get("/packs", response_model=List[Packs])
def consultar_packs()-> List[Packs]:
    result = Packs_services().consultar_packs()
    return result


# CONSULTAR UN PACK POR ID
@packs.get('/pack/{id}', response_model=Packs)
def consultar_pack_por_id(id:int) -> Packs:
    result = Packs_services().consultar_pack_por_id(id)
    return result


# AGREGAR UN NUEVO PACK
@packs.post("/packs", response_model=dict, dependencies=[Depends(JWTBearer())])
def agregar_pack(pack: Packs)-> dict:
    result = Packs_services().agregar_pack(pack)
    return result


# EDITAR UN PACK
@packs.put("/packs/{id}", response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def editar_pack(id: int, data: Packs)-> dict:
    result = Packs_services().editar_pack(id, data)
    return result


# BORRAR UN PACK
@packs.delete('/pack/{id}', response_model=dict, status_code=200)
def borrar_pack(id: int) -> dict:
    result = Packs_services().borrar_pack(id)
    return result