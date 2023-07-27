import random
import string
from fastapi.testclient import TestClient
from app import app



client = TestClient(app)

letras = string.ascii_lowercase
longitud_nombre = random.randint(5, 10)  # Longitud aleatoria del nombre entre 5 y 10 caracteres
nombre_nivel = ''.join(random.choice(letras) for _ in range(longitud_nombre))


#TEST CONSULTAR UN NIVEL
def test_agregar_un_nivel():
    data = {
            "id_nivel": 0,
            "nombre_nivel": nombre_nivel
            }

    response = client.post("/niveles", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado un nuevo nivel"}

#TEST CONSULTAR TODOS LOS NIVELES
def test_consultar_niveles():
    response = client.get("/niveles")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())





#TEST CONSULTAR UN PROFESOR
def test_consultar_un_nivel():
    nombre = nombre_nivel
    url = f"/nivel/{nombre}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
     
    
#TEST EDITAR UN NIVEL
def test_editar_un_():
    nombre = nombre_nivel
    url = f"/niveles/{nombre}"
    data = {
            "id_nivel":0,
            "nombre_nivel":nombre_nivel
           }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    


#TEST ELIMINAR UN Nivel
def eliminar_nivel():
    nombre = nombre_nivel
    url = f"/niveles/{nombre}"
    response = client.delete(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)