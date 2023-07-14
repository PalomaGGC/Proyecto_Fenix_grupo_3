from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from services.descuentos_services import Descuentos_services
from schemas.descuentos import Descuentos
from config.db import Base, engine

#RUTAS
descuentos = APIRouter(tags=["descuentos"])

#CREAR LAS TABLAS
@descuentos.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

#COSULTAR TODOS LOS DESCUENTOS
@descuentos.get("/descuentos")
async def consultar_todos_Descuentos():
    response = Descuentos_services().consultar_descuentos()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

#CONSULTAR UN DESCUENTO
@descuentos.get("/descuentos/{id}")
async def consultar_un_Descuentos(id):
    response = Descuentos_services().consultar_un_descuento(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

#AGREGAR UN NUEVO DESCUENTO
@descuentos.post("/descuentos")
async def crear_descuentos(descuento:Descuentos):
    response = Descuentos_services().crear_descuento(descuento)
    return response
    
#EDITAR UN DESCUENTO
@descuentos.put("/descuentos/{id}")
async def editar_descuentos(id, descuento:Descuentos):
    response = Descuentos_services().editar_descuento(id, descuento)
    return response 

