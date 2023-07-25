from fastapi.routing import APIRoute
import uvicorn
from fastapi import FastAPI, Body, Depends
from fastapi import APIRouter

from schemas.users import Users, UsersLogin
from middlewares.jwt_handler import signJWT



user = APIRouter(tags=["user"])

users = []

# Ruta para crear el usuario del login
@user.post("/user/signup", tags=["user"])
def create_user(user: Users = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


# Función para comprobar si existe un usuario antes de crear el login
def check_user(data: UsersLogin):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# Ruta para crear el login de usuario por primera vez
@user.post("/user/login", tags=["user"])
def user_login(user: UsersLogin = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }