from fastapi import FastAPI
from routers.alumnos_router import alumnos
from routers.packs_router import packs
from routers.descuentos_router import descuentos
from routers.inscripciones_router import inscripciones
from routers.profesores_router import profesores
from routers.niveles_router import niveles
from decouple import config
import uvicorn

app = FastAPI()
port = config("PORT") 

app.include_router(alumnos)
app.include_router(packs)
app.include_router(descuentos)
app.include_router(inscripciones)
app.include_router(profesores)
app.include_router(niveles)

if __name__ == '__main__':
    uvicorn.run("app:app", port=int(port), host='localhost', reload=True)


# https://github.com/AI-School-F5-P2/Proyecto_Fenix_equipo_3.gitgit remote -v