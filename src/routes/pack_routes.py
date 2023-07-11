import json
from fastapi import APIRouter
from config.db import conexion
from models.pack import tabla_pack
from schemas.pack import Packs
from sqlalchemy.exc import SQLAlchemyError

packs = APIRouter()

#COSULTAR
@packs.get("/packs", tags=["packs"])
def todosLosPacks():
    try:
        # Extraer todos los registros de la tabla "pack"
        query = tabla_pack.select()
        result = conexion.execute(query).fetchall()

        # Convertir los resultados a una lista de packs
        packs = []
        for item in result:
            pack = {
                "nombre_pack": item[1],
                "precio_pack": item[2]
            }
            packs.append(pack)

        # Retornar la lista de alumnos en formato JSON
        return packs
    except SQLAlchemyError as e:
        return {"error": str(e)}








#CONSULTAR SOLO UNO
@packs.get("/packs/{nombre}", tags=["packs"])
def obtenerPackPorNombre(nombre: int):
    try:
        # Buscar el pack por su nombre en la base de datos
        query = tabla_pack.select().where(tabla_pack.c.nombre_pack == nombre)
        result = conexion.execute(query).fetchone()

        # Verificar si se encontró un pack con el nombre especificado
        if result is None:
            return {"error": "No se encontró ningún pack con el nombre especificado."}

        # Crear un diccionario con los datos del pack
        pack = {
            "nombre_pack": result[1],
            "precio_pack": result[2]
        }

        # Retornar el pack en formato JSON
        return pack
    except SQLAlchemyError as e:
        return {"error": str(e)}






#AGREGAR
@packs.post("/packs", tags=["packs_agregar"])
def agregarPack(pack: Packs):
    try:
        # Verificar si el nombre del pack ya existe en la base de datos
        existe_pack = conexion.execute(tabla_pack.select().where(tabla_pack.c.nombre_alumno == pack.nombre_pack)).first()
        if existe_pack:
            return "No se puede agregar el pack. El pack ya está registrado."

        # Preparar los valores que se van a guardar
        nuevo_pack = {
            "nombre_pack": pack.nombre_pack,
            "precio_pack": pack.precio_pack
        }

        # Insertar el nuevo pack en la base de datos
        conexion.execute(tabla_pack.insert().values(**nuevo_pack))
        # Hacer un commit a la base de datos
        conexion.commit()

        return f"Se agregó el pack {nuevo_pack} correctamente"
    except SQLAlchemyError as e:
        return {"error": str(e)}
    
    
    
    
    


#EDITAR
@packs.put("/packs/{pack_id}", tags=["packs"])
def editarPack(pack_id: int, pack: Packs):
    try:
        # Verificar si el pack existe en la base de datos
        existe_pack = conexion.execute(tabla_pack.select().where(tabla_pack.c.id_pack == pack_id)).first()
        if not existe_pack:
            return {"error": "No se encontró ningún pack con el ID especificado."}

        # Preparar los valores que se van a actualizar
        valores_actualizados = {
            "nombre_pack": pack.nombre_pack,
            "precio_pack": pack.precio_pack
        }
        
        print(valores_actualizados)

        # Actualizar el pack en la base de datos
        query = tabla_pack.update().where(tabla_pack.c.id_pack == pack_id).values(**valores_actualizados)
        conexion.execute(query)
        conexion.commit()

        return {"message": "Pack actualizado correctamente."}
    except SQLAlchemyError as e:
        return {"error": str(e)}

