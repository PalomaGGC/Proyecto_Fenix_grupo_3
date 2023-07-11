from typing import Optional
from pydantic import BaseModel

class Packs(BaseModel):
    id_pack:Optional[int]