import random
import string
from fastapi.testclient import TestClient
from app import app



client = TestClient(app)

letras = string.ascii_lowercase
longitud_nombre = random.randint(5, 10)  # Longitud aleatoria del nombre entre 5 y 10 caracteres
nombre_clase= ''.join(random.choice(letras) for _ in range(longitud_nombre))

def test_agregar_pago():
    data = {
            "id_pago": 0,
            "inscripcion_id": 1,
            "fecha_pago": "2023-07-24"
           }

    response = client.post("/pagos", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado un nuevo pago correctamente"}



def test_consultar_pagos():
    response = client.get("/pagos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())


# def test_consultar_pago_por_id_del_alumno():
#     id = 1
#     url = f"/pagos/{id}"
#     response = client.get(url)
#     assert response.status_code == 200
#     assert all(isinstance(item, dict) for item in response.json())
     

    
    
