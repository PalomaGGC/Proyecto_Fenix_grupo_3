from typing import Optional
from pydantic import BaseModel

class Alumnos(BaseModel):

    nombre_alumno:str
    apellido_alumno:str
    edad_alumno:str
    nie_alumno:int
    email_alumno:str
    telefono_alumno:str
    descuento_familiar:float
    