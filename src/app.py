from fastapi import FastAPI
from routes.alumnos_routes import alumnos
from routes.pack_routes import packs

app = FastAPI()

app.include_router(alumnos)
app.include_router(packs)


# https://github.com/AI-School-F5-P2/Proyecto_Fenix_equipo_3.gitgit remote -v