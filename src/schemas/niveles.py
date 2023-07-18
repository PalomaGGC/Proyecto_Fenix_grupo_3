from typing import Optional
from pydantic import BaseModel

class Niveles(BaseModel):
    id_nivel:Optional[int]
    nombre_nivel:str
    
    
    
