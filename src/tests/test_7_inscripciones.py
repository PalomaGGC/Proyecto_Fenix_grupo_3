import random
import string
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_agregar_inscripcion():
    data = {
            "id_inscripcion": 0,
            "profesor_clase_id": 1,
            "alumno_id": 1,
            "precio_clase": "string",
            "descuento_inscripcion": 0,
            "descuento_familiar": 0,
            "precio_con_descuento": "string",
            "pagada": "false",
            "fecha_inscripcion": "2023-07-24"
            }

    response = client.post("/inscripcion", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado un nueva inscripción"}



def test_consultar_inscripciones():
    response = client.get("/inscripciones")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())
    
    
    
def test_consultar_inscripciones_pagas():
    id = 1
    bolean = "false"
    url = f"/inscripciones_pagadas/{id}?boleano={bolean}"
    response = client.get(url)
    assert response.status_code == 200
    assert all(isinstance(item, dict) for item in response.json())
    



def test_consultar_insripcion():
    id = 1
    url = f"/inscripcion/{id}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    
     
def test_editar_iscripcion():
    id = 1
    url = f"/inscripcion/{id}"
    data = {
            "id_inscripcion": 0,
            "profesor_clase_id": 1,
            "alumno_id": 1,
            "precio_clase": "string",
            "descuento_inscripcion": 0,
            "descuento_familiar": 0,
            "precio_con_descuento": "string",
            "pagada": "false",
            "fecha_inscripcion": "2023-07-24"
            }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha modificado la inscripción"}


#TEST ELIMINAR UN PACK
def eliminar_inscripcion():
    id = 1
    url = f"/inscripcion/{id}"
    response = client.delete(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha eliminado la inscripción"}