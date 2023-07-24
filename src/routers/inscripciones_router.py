from fastapi import APIRouter
from fastapi import FastAPI, HTTPException, Path, Query
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

#CONSULTAR UNA INSCRIPCION
@inscripciones.get("/inscripciones_pagadas/{id}")
async def consultar_inscripciones_pagas( id:int, boleano: bool ):
    # Llamar al servicio para consultar la inscripción con el ID y el valor booleano
    response = Inscripciones_services().consultar_inscripciones_pagadas(id, boleano)
    # Devolver la respuesta en formato JSON
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