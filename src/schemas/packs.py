from typing import Optional
from pydantic import BaseModel

class Packs(BaseModel):
    
    id_pack:Optional[int]
    nombre_pack:str
    precio_pack:float
    primer_descuento:float
    segundo_descuento:float