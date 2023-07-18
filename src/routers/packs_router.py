from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from config.db import Base, Session, engine
# from models.packsModel import Packs_model
from schemas.packs import Packs
from services.packs_services import Packs_services

packs = APIRouter(tags=["packs"])

@packs.on_event("startup")
def startup():
    # create db table
    Base.metadata.create_all(bind=engine)

#COSULTAR
@packs.get("/packs", response_model=List[Packs], status_code=200)
def consultar_packs()-> List[Packs]:
    result = Packs_services().consultar_packs()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


#CONSULTAR SOLO UNO
@packs.get('/pack/{id}', response_model=Packs)
def consultar_pack_por_id(id:int) -> Packs:
    result = Packs_services().consultar_pack(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


#AGREGAR
@packs.post("/packs", response_model=dict, status_code=201)
def agregar_pack(pack: Packs)-> dict:
    Packs_services().agregar_pack(pack)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo pack"})


#EDITAR
@packs.put("/packs/{id}", response_model=dict, status_code=200)
def editar_pack(id: int, data: Packs)-> dict:
    result = Packs_services().consultar_pack(id)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    Packs_services().editar_pack(id, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el pack"})

#BORRAR
@packs.delete('/packs/{id}', response_model=dict, status_code=200)
def borrar_pack(id: int) -> dict:
    result = Packs_services().consultar_pack(id)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    Packs_services().borrar_pack(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el pack"})

