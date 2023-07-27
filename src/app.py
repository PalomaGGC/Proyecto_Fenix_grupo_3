from models.pagosModel import Pagos_model
from services.incripcion_automatica_services import crear_nueva_inscripcion
from routers.profesor_clases_router import profesor_clases
from routers.inscripciones_router import inscripciones
from routers.profesores_router import profesores
from services.incripcion_automatica_services import ejecutar_funcion_en_hora_especifica
from routers.users_router import user
from routers.alumnos_router import alumnos
from routers.niveles_router import niveles
from routers.clases_router import clases
from routers.clases_router import clases
from routers.packs_router import packs
from routers.pagos_router import pagos 
from config.db import Base, engine
from fastapi import FastAPI
from decouple import config
import threading
import schedule
import uvicorn
import time
from middlewares.error_handler import ErrorHandler # Importamos el manejador de errores

port = config("PORT") 
app = FastAPI()

app.add_middleware(ErrorHandler)
app.include_router(user)
app.include_router(profesor_clases)
app.include_router(inscripciones)
app.include_router(profesores)
app.include_router(niveles)
app.include_router(alumnos)
app.include_router(clases)
app.include_router(packs)
app.include_router(pagos)

Base.metadata.create_all(bind=engine)

# Define la hora y minuto específicos para la ejecución (ejemplo: 15:30)
hora_especifica = 00
minuto_especifico = 00
segundos = 00

# Ejecuta la función en la hora determinada
ejecutar_funcion_en_hora_especifica(hora_especifica, minuto_especifico, segundos)

# uvicorn app:app --host localhost --port 5000 --reload



