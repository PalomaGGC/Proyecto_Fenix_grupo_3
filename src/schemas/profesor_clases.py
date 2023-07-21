from typing import Optional
from pydantic import BaseModel

class Profesor_clases(BaseModel):

    id_clase_profesor : Optional[int]
    clase_id:int
    profesor_id:int
    nivel_id:int
