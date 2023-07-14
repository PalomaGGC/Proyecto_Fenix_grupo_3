from fastapi import APIRouter
from services.descuentos_services import Descuentos_services
from schemas.descuentos import Descuentos
from config.db import Session

'''

descuentos = APIRouter(tags=["descuentos"])


#COSULTAR
@descuentos.get("/descuentos")
async def todosLosDescuentos():
    descuento = Descuentos_services()
    result = descuento.descuento()
    return result



#CONSULTAR SOLO UNO
@descuentos.get("/descuento/{id}")
async def obtenerUnDescuento(id: int):
    descuento = Descuentos_services()
    result = descuento.descuento(id)
    return result


#AGREGAR
@descuentos.post("/descuentos")
async def agregarDescuento(descuento:Descuentos):
    descuentos = Descuentos_services()
    result = descuentos.agregar_descuento(descuento)
    return result
    
    
    
# #EDITAR
@descuentos.put("/descuento/{id}")
def editarDescuento(id: int, descuento:Descuentos):
    descuentos = Descuentos_services()
    result = descuentos.editar_descuento(id, descuento)
    return result

    
    '''