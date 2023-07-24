#from services.incripcion_automatica_services import crear_nueva_inscripcion
from routers.profesor_clases_router import profesor_clases
from routers.inscripciones_router import inscripciones
from routers.profesores_router import profesores
from routers.alumnos_router import alumnos
from routers.niveles_router import niveles
from routers.clases_router import clases
from routers.clases_router import clases
from routers.packs_router import packs
from config.db import Base, engine
from fastapi import FastAPI
from decouple import config
import threading
#import schedule
import uvicorn
import time
from middlewares.error_handler import ErrorHandler # Importamos el manejador de errores

port = config("PORT") 
app = FastAPI()

app.add_middleware(ErrorHandler)
app.include_router(profesor_clases)
app.include_router(inscripciones)
app.include_router(profesores)
app.include_router(niveles)
app.include_router(alumnos)
app.include_router(clases)
app.include_router(packs)

Base.metadata.create_all(bind=engine)

#GENERAR NUEVAS INSCRIPCIONES AUTOMATICAMENTE
def programar_creacion_nueva_inscripcion():
    schedule.every().day.at("00:00:00").do(crear_nueva_inscripcion)
    # Programo la ejecución de la función "crear_nueva_inscripcion" cada día a la medianoche
    while True:
        schedule.run_pending()
        time.sleep(1)
        
# Utilizo threading para ejecutar la función en un hilo separado
creacion_inscripciones_thread = threading.Thread(target=programar_creacion_nueva_inscripcion)
creacion_inscripciones_thread.start()

# uvicorn app:app --host localhost --port 5000 --reload