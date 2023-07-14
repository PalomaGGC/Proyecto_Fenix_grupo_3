from typing import Optional
from pydantic import BaseModel

class Niveles(BaseModel):
    id_niveles:Optional[int]
    nombre_nivel:str
    