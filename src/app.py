from fastapi import FastAPI
from routers.alumnos_router import alumnos
from routers.pack_router import packs
from routers.descuentos_router import descuentos

app = FastAPI()

app.include_router(alumnos)
app.include_router(packs)
app.include_router(descuentos)


# https://github.com/AI-School-F5-P2/Proyecto_Fenix_equipo_3.gitgit remote -v