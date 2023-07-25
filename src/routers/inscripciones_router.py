from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.inscripciones import Incripciones
from services.inscripciones_services import  Inscripciones_services

# RUTAS
inscripciones = APIRouter(tags=["inscripciones"])


# COSULTAR TODAS LAS INSCRIPCIONES
@inscripciones.get("/inscripciones")
async def consultar_Inscripciones():
    result = Inscripciones_services().consultar_inscripciones()
    return result


# CONSULTAR UNA INSCRIPCIÓN POR ID
@inscripciones.get("/inscripcion/{id}")
async def consultar_una_inscripcion(id):
    result = Inscripciones_services().consultar_una_inscripcion(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# CONSULTAR INSCRIPCIONES PAGADAS POR ID ALUMNO
@inscripciones.get("/inscripciones_pagadas/{id}")
async def consultar_inscripciones_pagas( id:int, boleano: bool ):
    # Llamar al servicio para consultar la inscripción con el ID y el valor booleano
    result = Inscripciones_services().consultar_inscripciones_pagadas(id, boleano)
    return result


# CREAR UNA NUEVA INSCRIPCIÓN
@inscripciones.post("/inscripcion")
async def crear_inscripcion(data:Incripciones):
    results = Inscripciones_services().crear_inscripcion(data)
    return results


# EDITAR UNA INSCRIPCIÓN
@inscripciones.put("/inscripcion/{id}")
async def editar_inscripcion(id, data:Incripciones):
    result = Inscripciones_services().editar_inscripcion(id, data)
    return result


# ELIMINAR INSCRIPCION
@inscripciones.delete("/inscripcion/{id}")
async def eliminar_inscripcion(id):
    response = Inscripciones_services().eliminar_inscripcion(id)
    return response 