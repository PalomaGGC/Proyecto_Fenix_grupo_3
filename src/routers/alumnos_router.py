from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError
from services.alumnos_services import Alumnos_services
from config.db import Base, Session, engine


alumnos = APIRouter(tags=["alumnos"])

#CREAR LAS TABLAS
@alumnos.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


#COSULTAR
@alumnos.get("/alumnos", response_model=List[Alumnos], status_code=200)
def todosLosAlumnos() -> List[Alumnos]:
    db = Session()
    result = Alumnos_services(db).consultar_alumnos()
    
    if not result:
        return None
    
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alumnos.get('/alumno/{nie}', response_model=Alumnos)# nie es el parámetro de ruta que es pero recibir cuanod el usuario acceda  a esta url
def consultar_alumno_nie(nie:str) -> Alumnos:
    db = Session()
    #Creo una sesión para conectarme a la base de datos, la variable db será una instancia de session, que ya importé al inicio
    result = Alumnos_services(db).consultar_alumno(nie)
    #De Alumnos_services primero obtengo la sesión y luego le paso el método consultar_alumno
    #Consulto los datos de AlumnoModel y hago un filtrado por nie, le digo que obtenga el primer resultado.
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@alumnos.post("/alumnos", response_model=dict, status_code=201)
def agregarAlumno(alumno: Alumnos) -> dict:
    db = Session()
    Alumnos_services(db).agregar_alumno(alumno)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo alumno"})



@alumnos.put('/alumnos/{nie}', response_model=dict, status_code=200)
def editarAlumno(nie: str, data:Alumnos) -> dict:
    db = Session()
    result = Alumnos_services(db).consultar_alumno(nie)
    if not result:
         return JSONResponse(status_code=404, content={'message': "No encontrado"})

    Alumnos_services(db).editar_alumno(nie, data)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el alumno"})





