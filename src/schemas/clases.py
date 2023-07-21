from typing import Optional
from pydantic import BaseModel

class Clases(BaseModel):
    
    id_clase: Optional[int]
    nombre_clase: str
    packs_id: int
