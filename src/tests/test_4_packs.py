import random
import string
from fastapi.testclient import TestClient
from app import app



client = TestClient(app)

letras = string.ascii_lowercase
longitud_nombre = random.randint(5, 10)  # Longitud aleatoria del nombre entre 5 y 10 caracteres
nombre_pack = ''.join(random.choice(letras) for _ in range(longitud_nombre))


#TEST AGREGAR UN PACK
def test_agregar_un_pack():
    data = {
            "id_pack": 0, "nombre_pack": nombre_pack,
            "precio_pack": 0,
            "primer_descuento": 0,
            "segundo_descuento": 0
            }

    response = client.post("/packs", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado un nuevo pack"}


#TEST CONSULTAR TODOS LOS PACKS
def test_consultar_packs():
    response = client.get("/packs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(isinstance(item, dict) for item in response.json())


#TEST CONSULTAR UN PACK
def test_consultar_un_pack():
    id = 1
    url = f"/pack/{id}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
     
     
#TEST EDITAR UN PACK
def test_editar_un_pack():
    id = 1
    url = f"/packs/{id}"
    data = {
            "id_pack":0,
            "nombre_pack": nombre_pack + " esditado",
            "precio_pack": 0,
            "primer_descuento": 0,
            "segundo_descuento": 0
            }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha modificado el pack"}


#TEST ELIMINAR UN PACK
def eliminar_PACK():
    id = 1
    url = f"/packs/{id}"
    response = client.delete(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha eliminado el pack"}