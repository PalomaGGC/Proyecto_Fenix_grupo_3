from fastapi.testclient import TestClient
from app import app



client = TestClient(app)





def test_agregar_un_alumno():
    data = {
            "id_alumno": 0,        
            "apellido_alumno": "Apellido prueba",
            "edad_alumno": "20",
            "email_alumno": "email prueba",
            "nombre_alumno": "Nombre prueba",   
            "telefono_alumno": "123456789",
            "descuento_familiar": 0
            }
    
    response = client.post("/alumnos", json=data)
    assert response.status_code == 201
    assert response.json() == {"message": "Se ha registrado un nuevo alumno"}




# #TODOS LOS ALUMNOS
def test_consultar_alumnos():
    response = client.get("/alumnos")
    # Realizo una solicitud GET a la ruta "/alumnos" utilizando -
    # el cliente de prueba client que se ha configurado previamente
    assert response.status_code == 200
    # Verifico que el código de estado de la respuesta sea 200, -
    # lo que indica que la solicitud fue exitosa.
    assert isinstance(response.json(), list)
    # Verifico que el JSON de la respuesta sea una instancia de la -
    # list, es decir, verifica que la respuesta sea una lista.
    assert all(isinstance(item, dict) for item in response.json())
    # Utilizo la función all() para verificar que todos los elementos -
    # en la lista de JSON sean instancias de la clase dict, es decir, -
    # verifica que cada elemento de la lista sea un diccionario.




# #UN ALUMNO
def test_consultar_un_alumno():
    
    id = 1
    url = f"/alumno/{id}"
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    #Esta vez espero que retorne un diccionario
    
    
    
    
#TEST EDITAR ALUMNO
def test_editar_un_alumno():
    id = 1
    url = f"/alumnos/{id}"
    data = {
            "id_alumno": 0,
            "nombre_alumno": "string",
            "apellido_alumno": "string",
            "edad_alumno": "30",
            "email_alumno": "string",
            "telefono_alumno": "string",
            "descuento_familiar": 0
            }
    response = client.put(url, json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha modificado el alumno"}
    


#TEST ELIMINAR ALUMNO
def eliminar_alumno():
    id = 1
    url = f"/alumnos/{id}"
    response = client.delete(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Se ha eliminado el alumno"}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#pytest