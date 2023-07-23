import schedule
import uvicorn
from fastapi import FastAPI
import threading
from fastapi.testclient import TestClient
from routers.alumnos_router import alumnos
from routers.clases_router import clases
from routers.packs_router import packs
from routers.inscripciones_router import inscripciones
from routers.profesores_router import profesores
from routers.profesor_clases_router import profesor_clases
from routers.clases_router import clases
from routers.niveles_router import niveles
from decouple import config
from config.db import Base, engine
from services.incripcion_automatica_services import crear_nueva_inscripcion
import time

app = FastAPI()
port = config("PORT") 

app.include_router(alumnos)
app.include_router(clases)
app.include_router(niveles)
app.include_router(packs)
app.include_router(profesores)
app.include_router(inscripciones)
app.include_router(profesor_clases)

Base.metadata.create_all(bind=engine)

#GENERAR NUEVAS INSCRIPCIONES AUTOMATICAMENTE
def programar_creacion_nueva_inscripcion():
    schedule.every().day.at("19:20:10").do(crear_nueva_inscripcion)
    # Programo la ejecución de la función "crear_nueva_inscripcion" cada día a la medianoche
    while True:
        schedule.run_pending()
        time.sleep(1)
        
# Utilizo threading para ejecutar la función en un hilo separado
creacion_inscripciones_thread = threading.Thread(target=programar_creacion_nueva_inscripcion)
creacion_inscripciones_thread.start()

# uvicorn app:app --host localhost --port 5000 --reload