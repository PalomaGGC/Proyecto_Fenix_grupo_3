from fastapi.routing import APIRoute
import uvicorn
from fastapi import FastAPI, Body, Depends
from fastapi import APIRouter

from schemas.users import Users, UsersLogin
from middlewares.jwt_handler import signJWT
from services.users_services import create_user_service, user_login_service



user = APIRouter(tags=["user"])

users = []

# Ruta para crear el usuario del login
@user.post("/user/signup", tags=["user"])
def create_user(user: Users = Body(...)):
    result = create_user_service(user)
    return result


# Ruta para crear el login de usuario por primera vez
@user.post("/user/login", tags=["user"])
def user_login(user: UsersLogin = Body(...)):
    result = user_login_service(user)
    return result
