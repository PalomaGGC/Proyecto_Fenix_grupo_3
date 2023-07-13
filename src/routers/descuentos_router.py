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


# #AGREGAR
# @descuentos.post("/descuentos")
# def agregarAlumno(descuento:Descuentos):
#     descuentos = Descuentos_services()
#     result = descuentos.agregar_descuento(descuento)
#     return result
    
    

# #EDITAR
# @alumnos.put("/descuento/{id}")
# def editarAlumno(alumno_id: int, alumno: Alumnos):
#     alumnos = Alumnos_services()
#     result = alumnos.editar_alumno(alumno_id, alumno)
#     return result
