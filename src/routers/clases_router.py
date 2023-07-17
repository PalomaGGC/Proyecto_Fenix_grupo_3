from fastapi import APIRouter
from config.db import conexion
from models.clasesModel import tabla_clases
from schemas.alumnos import Alumnos
from sqlalchemy.exc import SQLAlchemyError


user = APIRouter()

@user.get("/")
async def read_data():
    return conexion.execute(users.select()).fetchall()


@user.get("/{id}")
async def read_data(id: int):
    
    return conexion.execute(users.select().where(user.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
    conexion.execute(users.insert().values(
        

    ))
    return conn.execute(users.select()).fetchall()


@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update(
        name=user.name,
        email=user.email,
        password=user.password

    ).where(user.c.id == id))

    return conn.execute(users.select()).fetchall()

@user.get("/")
async def delete_data():
    conn.execute(users.delete().where(user.c.id == id))
    return conn.execute(users.select()).fetchall()