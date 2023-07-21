from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.profesor_clases import Profesor_clases
from schemas.profesor_clases import Profesor_clases
from services.profesor_clases_services import Profesor_clases_services
from config.db import Base, engine


profesor_clases = APIRouter(tags=["profesor_clases"])

 #CREAR LAS TABLAS
@profesor_clases.on_event("startup")
def startup():
  Base.metadata.create_all(bind=engine)

# COSULTAR TODAS LAS RELACIONES 'PROFESOR - CLASE - NIVEL'
@profesor_clases.get("/profesor-clases", response_model=List[Profesor_clases], status_code=200)
def consultar_todas_profesor_clases() -> List[Profesor_clases]:
    result = Profesor_clases_services().consultar_profesor_clases()

    if not result:
        return None

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


# CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
@profesor_clases.get('/profesor-clases/{id}', response_model=Profesor_clases)# id es el parámetro de ruta que espero recibir cuando el usuario acceda  a esta url
def consultar_profesor_clase_por_id(id: int) -> Profesor_clases:
    result = Profesor_clases_services().consultar_profesor_clase(id)
    #Consulto los datos de Profesor_clases_model y hago un filtrado por id, le digo que obtenga el primer resultado.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# AÑADO UN NUEVO PROFESOR A LA TABLA
@profesor_clases.post("/profesor-clases", response_model=dict, status_code=201)
def agregar_profesor_clase(data: Profesor_clases) -> dict:
    Profesor_clases_services().agregar_profesor_clase(data)
    return JSONResponse(status_code=201, content={"message": "Se ha agregado una nueva relación 'profesor -clase - nivel' correctamente"})


# MODIFICO LOS DATOS DE UN PROFESOR
@profesor_clases.put('/profesor-clases/{id}', response_model=dict, status_code=200)
def editar_profesor_clase(id: int, data:Profesor_clases) -> dict:
    result = Profesor_clases_services().consultar_profesor_clase(id)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})

    Profesor_clases_services().editar_profesor_clase(id, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la relación 'profesor - clase -nivel' correctamente"})

# BORRO UN PROFESOR
@profesor_clases.delete('/profesor-clases/{id}', response_model=dict, status_code=200)
def borrar_profesor_clase(id: int) -> dict:
    result = Profesor_clases_services().consultar_profesor_clase(id)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    Profesor_clases_services().borrar_profesor_clase(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la relación 'profesor - clase -nivel' correctamente"})


