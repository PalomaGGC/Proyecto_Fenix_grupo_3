from typing import Optional
from pydantic import BaseModel

class Alumnos(BaseModel):

    id_alumno : Optional[int]
    nombre_alumno:str
    apellido_alumno:str
    edad_alumno:str
    email_alumno:str
    telefono_alumno:str
    descuento_familiar:float


