from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.descuentos import Descuentos
from services.inscripciones_services import  Inscripciones_services
from config.db import Base, engine

#RUTAS
inscripciones = APIRouter(tags=["inscripciones"])

#CREAR LAS TABLAS
# @inscripciones.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)
    
#COSULTAR TODOS LAS INSCRIPCIONES
@inscripciones.get("/inscripciones")
async def consultar_Inscripciones():
    response = Inscripciones_services().consultar_inscripciones()
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

#CONSULTAR UNA INSCRIPCION
@inscripciones.get("/inscripcion/{id}")
async def consultar_una_inscripcion(id):
    response = Inscripciones_services().consultar_una_inscripcion(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(response))


# @inscripciones.post("/inscripcion")
# async def consultar_una_inscripcion():
#     response = Inscripciones_services().crear_inscripcion()
#     return response

# #AGREGAR UNA NUEVA INSCRIPCION
# @descuentos.post("/descuentos")
# async def crerar_descuentos(descuento:Descuentos):
#     response = Descuentos_services().crear_descuento(descuento)
#     return response
    
# #EDITAR UNA INSCRIPCION
# @descuentos.put("/descuentos/{id}")
# async def editar_descuentos(id, descuento:Descuentos):
#     response = Descuentos_services().editar_descuento(id, descuento)
#     return response 
