from typing import Optional
from pydantic import BaseModel

class Profesores(BaseModel):

    id_profesor : Optional[int]
    nombre_profesor:str
    apellido_profesor:str
    email_profesor:str

