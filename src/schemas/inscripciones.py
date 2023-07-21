from typing import Optional
from pydantic import BaseModel

class Incripciones(BaseModel):

    id_inscripciones : Optional[int]
    profesor_clase_id:int
    alumno_id:int
    precio_clase:str
    nie_alumno:str
    descuento_inscripcion:float
    precio_con_descuento:str
    estado_inscripcion:float
    fecha_inscripcion:str