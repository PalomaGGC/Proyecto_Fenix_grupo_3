from fastapi import APIRouter
from services.descuentos_services import Descuentos_services
from schemas.descuentos import Descuentos




descuentos = APIRouter(tags=["descuentos"])


#COSULTAR
@descuentos.get("/descuentos")
def todosLosAlumnos():
    descuento = Descuentos_services()
    result = descuento.descuento()
    return result



#CONSULTAR SOLO UNO
@descuentos.get("/descuento/{id}")
def obtenerAlumnoPorNIE(id: int):
    descuento = Descuentos_services()
    result = descuento.descuento(id)
    return result


#AGREGAR
@descuentos.post("/descuentos")
def agregarAlumno(descuento:Descuentos):
    descuentos = Descuentos_services()
    result = descuentos.agregar_descuento(descuento)
    return result
    
    

# #EDITAR
@descuentos.put("/descuento/{id}")
def editarAlumno(id: int, descuento:Descuentos):
    descuentos = Descuentos_services()
    result = descuentos.editar_descuento(id, descuento)
    return result
