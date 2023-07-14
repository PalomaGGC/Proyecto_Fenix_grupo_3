from fastapi import FastAPI
from routers.alumnos_router import alumnos
from routers.pack_router import packs
#from routers.descuentos_router import descuentos
from decouple import config
import uvicorn

app = FastAPI()
port = config("PORT")

app.include_router(alumnos)
app.include_router(packs)
#app.include_router(descuentos)


if __name__ == '__main__':
    uvicorn.run("app:app", port=int(port), host='localhost', reload=True)


# https://github.com/AI-School-F5-P2/Proyecto_Fenix_equipo_3.gitgit remote -v