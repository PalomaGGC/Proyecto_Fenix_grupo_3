from typing import Optional
from pydantic import BaseModel

class Class(BaseModel):
    nombre_clase: str
    pack_id: str