import random
import string
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


#TEST AGREGAR UN NUEVO CLASE_PROFESOR
def test_agregar_clase_profesor():
    data = {
            "id_clase_profesor": 0,
            "clase_id": 1,
            "profesor_id": 1,
            "nivel_id": 1
            }

    response = client.post("/profesores-clases", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado una nueva relación 'profesor - clase -nivel' "}


# COSULTAR TODAS LAS RELACIONES 'PROFESOR - CLASE - NIVEL'
def test_consultar_clases_profesores():
    response = client.get("/profesor-clases")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())


#TEST CONSULTAR UN CLASE_PROFESOR POR ID_CLASE_PROFESOR
def test_consultar_profesor_clase_nivel_por_id():
    id = 1
    url = f"/profesor-clases/{id}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    
     
#TEST EDITAR CLASE_PROFESOR
def test_editar_clase_profesor():
    id = 1
    url = f"/profesor-clases/{id}"
    data = {
            "id_clase_profesor": 0,
            "clase_id": 1,
            "profesor_id": 1,
            "nivel_id": 1
            }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Relación 'profesor - clase -nivel' actualizada correctamente"}


#TEST ELIMINAR UN PACK
def eliminar_PACK():
    id = 1
    url = f"/packs/{id}"
    response = client.delete(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha eliminado el pack"}