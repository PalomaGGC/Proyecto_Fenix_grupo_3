from typing import Optional
from pydantic import BaseModel

class Descuentos(BaseModel):
    id_descuentos:Optional[int]
    tipo_descuentos: str
    porcentage_descuento: int