from fastapi import FastAPI
from routes.alumnos_routes import alumnos

app = FastAPI()

app.include_router(alumnos)


