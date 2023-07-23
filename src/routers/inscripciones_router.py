from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.inscripciones import Incripciones
from services.inscripciones_services import  Inscripciones_services
from config.db import Base, engine

#RUTAS
inscripciones = APIRouter(tags=["inscripciones"])


    
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


@inscripciones.post("/inscripcion")
async def crear_inscripcion(data:Incripciones):
    results = Inscripciones_services().crear_inscripcion(data)
    return JSONResponse(status_code=200, content=jsonable_encoder(results))

    
#EDITAR UNA INSCRIPCION
@inscripciones.put("/descuentos/{id}")
async def editar_inscripcion(id, data:Incripciones):
    response = Inscripciones_services().editar_inscripcion(id, data)
    return response 


# ELIMINAR INSCRIPCION
@inscripciones.delete("/descuentos/{id}")
async def editar_inscripcion(id):
    response = Inscripciones_services().eliminar_inscripcion(id)
    return response 