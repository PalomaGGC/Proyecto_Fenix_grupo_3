# Este archivo se encarga de logear, codificar, decodifcar y devolver JWTS

import time #Los tokens tienen una durabilidad, con time marcamos la expiración
from typing import Dict

import jwt #responsable del codificar y decodificar
from decouple import config #ayuda a organizar tus settings para que puedas cambiar parámetros


JWT_SECRET = config("SECRET")
JWT_ALGORITHM = config("ALGORITHM")

# Función que devuelve el token generado (JWTs)
def token_response(token: str):
    return {
        "access_token": token
    }

# Función usada para el signing o registro de JWT string
def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600 #la hoara a la que se registra y 600 milisegundos
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    #En la variable token se guarda el payload + la secret key codificados por el algoritmo elegido (HS256)
    return token_response(token)

# Función para decodificar el JWT
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        #En la variable decoded_token se guarda el payload + la secret key decodificados por el algoritmo elegido (HS256)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}