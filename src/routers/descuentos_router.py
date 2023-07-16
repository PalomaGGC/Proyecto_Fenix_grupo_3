from typing import Dict, List, Any
from config.db import Base, engine
from fastapi import APIRouter, Header
from schemas.descuentos import Descuentos
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.descuentos_services import Descuentos_services

#RUTAS
descuentos = APIRouter(tags=["descuentos"])

#CREAR LAS TABLAS
@descuentos.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

#COSULTAR TODOS LOS DESCUENTOS
@descuentos.get("/descuentos" , response_model=List[Descuentos])
async def consultar_todos_Descuentos():
    response = Descuentos_services().consultar_descuentos()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

#CONSULTAR UN DESCUENTO
@descuentos.get("/descuentos/{id}", response_model=Descuentos)
async def consultar_un_Descuentos(id):
    response = Descuentos_services().consultar_un_descuento(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

#AGREGAR UN NUEVO DESCUENTO
@descuentos.post("/descuentos", response_model=Descuentos)
async def crear_descuentos(descuento:Descuentos):
    response = Descuentos_services().crear_descuento(descuento)
    return JSONResponse(status_code=201, content=jsonable_encoder(response))
    
#EDITAR UN DESCUENTO
@descuentos.put("/descuentos/{id}", response_model=Descuentos)
def editar_descuentos(id, descuento:Descuentos, ):
    response = Descuentos_services().editar_descuento(id, descuento)
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

