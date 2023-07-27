from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from schemas.profesor_clases import Profesor_clases
from schemas.profesor_clases import Profesor_clases
from services.profesor_clases_services import Profesor_clases_services
from config.db import Base, engine


profesor_clases = APIRouter(tags=["profesor_clases"])

 # CREAR LAS TABLAS DE PROFESOR - CLASES -NIVEL
@profesor_clases.on_event("startup")
def startup():
  Base.metadata.create_all(bind=engine)


# COSULTAR TODAS LAS RELACIONES 'PROFESOR - CLASE - NIVEL'
@profesor_clases.get("/profesor-clases", response_model=List[Profesor_clases])
def consultar_todas_profesor_clases() -> List[Profesor_clases]:
    result = Profesor_clases_services().consultar_profesor_clases()
    return result


# CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
@profesor_clases.get('/profesor-clases/{id}', response_model=Profesor_clases)# id es el parámetro de ruta que espero recibir cuando el usuario acceda  a esta url
def consultar_profesor_clase_nivel_por_id(id: int) -> Profesor_clases:
    result = Profesor_clases_services().consultar_profesor_clase_nivel_por_id(id)
    #Consulto los datos de Profesor_clases_model y hago un filtrado por id, le digo que obtenga el primer resultado.
    return result


# CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR EL NOMBRE DE LA CLASE
@profesor_clases.get("/profesor-clases-nivel-por-clase/{nombre}", response_model=List[Profesor_clases])
def consultar_profesor_clase_nivel_por_nombre_clase(nombre: str):
    result = Profesor_clases_services().consultar_profesor_clase_nivel_por_nombre_clase(nombre)
    return result


# CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR EL NOMBRE DEL PROFESOR
@profesor_clases.get("/profesor-clases-nivel-por-profesor/{nombre}", response_model=List[Profesor_clases])
def consultar_profesor_clase_nivel_por_nombre_profesor(nombre: str):
    result = Profesor_clases_services().consultar_profesor_clase_nivel_por_nombre_profesor(nombre)
    return result


# AÑADIR UNA NUEVA RELACIÓN 'PROFESOR - CLASE - NIVEL'
@profesor_clases.post("/profesor-clases", response_model=dict)
def agregar_profesor_clase_nivel(data: Profesor_clases) -> dict:
    result = Profesor_clases_services().agregar_profesor_clase_nivel(data)
    return result


# MODIFICAR LOS DATOS DE UNA RELACIÓN 'PROFESOR - CLASE - NIVEL'
@profesor_clases.put('/profesor-clases/{id}', response_model=dict, dependencies=[Depends(JWTBearer())])
def editar_profesor_clase_nivel(id: int, data:Profesor_clases) -> dict:
    result = Profesor_clases_services().editar_profesor_clase_nivel(id, data)
    return result


# BORRAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL'
@profesor_clases.delete('/profesor-clases/{id}', response_model=dict, dependencies=[Depends(JWTBearer())])
def borrar_profesor_clase_nivel(id: int) -> dict:
    result = Profesor_clases_services().borrar_profesor_clase_nivel(id)
    return result


