from fastapi import APIRouter

alumnos = APIRouter()

@alumnos.get("/alumnos", tags=["alumnos"])
def todosLosAlumnos():
    
    return "alumnos"