import random
import string
from fastapi.testclient import TestClient
from app import app



client = TestClient(app)

letras = string.ascii_lowercase
longitud_nombre = random.randint(5, 10)  # Longitud aleatoria del nombre entre 5 y 10 caracteres
nombre_clase= ''.join(random.choice(letras) for _ in range(longitud_nombre))

def test_agregar_una_clase():
    data = {
            "id_clase": 0,
            "nombre_clase": nombre_clase,
            "packs_id": 1
            }

    response = client.post("/clases", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado una nueva clase"}


#TEST CONSULTAR TODOS LAS CLASES
def test_consultar_clases():
    response = client.get("/clases")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())



# #TEST CONSULTAR UNA CLASE
def test_consultar_una_clase():
    id = 1
    url = f"/clase/{id}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
     
    
# TEST EDITAR UNA CLASE
def test_editar_una_clase():
    id = 1
    url = f"/clases/{id}"
    data = {"id_clase":0,
            "nombre_clase": "bachata",
            "packs_id": 1
            }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    


# #TEST ELIMINAR UNA CLASE
def eliminar_profesor():
    id = 1
    url = f"/clases/{id}"
    response = client.delete(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    
    
    
