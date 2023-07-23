from typing import Optional
from pydantic import BaseModel

class Incripciones(BaseModel):

    id_inscripcion : Optional[int]
    profesor_clase_id:int
    alumno_id:int
    precio_clase:str
    descuento_inscripcion:float
    descuento_familiar:float
    precio_con_descuento:str
    estado_inscripcion:str
    fecha_inscripcion:str