from datetime import date
from typing import Optional
from pydantic import BaseModel

class Pagos(BaseModel):
    
    id_pago:Optional[int]
    inscripcion_id:int
    fecha_pago:date

    
    
    