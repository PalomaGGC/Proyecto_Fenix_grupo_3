import random
import string
from fastapi.testclient import TestClient
from app import app



client = TestClient(app)

letras = string.ascii_lowercase
longitud_nombre = random.randint(5, 10)  # Longitud aleatoria del nombre entre 5 y 10 caracteres
nombre_aleatorio = ''.join(random.choice(letras) for _ in range(longitud_nombre))



#TEST AGREGAR UN PROFESOR
def test_agregar_un_profesor():
    data = {
            "id_profesor": 0,
            "nombre_profesor": nombre_aleatorio,
            "apellido_profesor": "string",
            "email_profesor": "string"
            }

    response = client.post("/profesores", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado un nuevo profesor"}


#TEST CONSULTAR TODOS LOS PROFESORES
def test_consultar_profesores():
    response = client.get("/profesores")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())


#TEST CONSULTAR UN PROFESOR
def test_consultar_un_profesor():
    nombre = nombre_aleatorio
    url = f"/profesor/{nombre}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
     
    
#TEST EDITAR UN PROFESOR
def test_editar_un_profesor():
    nombre = nombre_aleatorio
    url = f"/profesores/{nombre}"
    data = {
            "id_profesor": 0,
            "nombre_profesor": nombre_aleatorio,
            "apellido_profesor": "string",
            "email_profesor": "string"
            }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    


# #TEST ELIMINAR UN PROFESOR
def eliminar_profesor():
    nombre = nombre_aleatorio
    url = f"/profesores/{nombre}"
    response = client.delete(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)