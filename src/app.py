from fastapi import FastAPI
from routes.alumnos_routes import alumnos

app = FastAPI()

app.include_router(alumnos)


# https://github.com/AI-School-F5-P2/Proyecto_Fenix_equipo_3.gitgit remote -v