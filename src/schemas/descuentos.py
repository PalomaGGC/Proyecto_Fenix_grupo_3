from typing import Optional
from pydantic import BaseModel

class Descuentos(BaseModel):
    id_descuento:Optional[int]
    tipo_descuento: str
    porcentage_descuento: int