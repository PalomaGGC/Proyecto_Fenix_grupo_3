from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.clasesModel import Clases_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session


class Clases_services:
    def __init__(self):
        self.db = Session()


    # CONSULTAR TODAS LOS CLASSES
    def consultar_clases(self):
        result = self.db.query(Clases_model).all()
        #obtengo todos los datos Clases_model y los guardo en la variable result
        if not result:
        # Si no se encuentran clases, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aún no hay clases") 
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UN CLASE
    def consultar_clase_por_id(self, id):
        result = self.db.query(Clases_model).filter(Clases_model.id_clase == id).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ninguna clase con ese id")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # AGREGAR UNA NUEVA CLASE
    def agregar_clase(self, data):
        clase = self.db.query(Clases_model).filter(Clases_model.nombre_clase == data.nombre_clase).first()
        if clase:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe una clase con este nombre")
        nueva_clase = Clases_model(**data.dict())
        self.db.add(nueva_clase)
        self.db.commit()
        return JSONResponse(status_code=201, content={"message": "Se ha registrado una nueva clase"})


    # EDITAR UNA CLASE
    def editar_clase(self, id: int, data):
        clase = self.db.query(Clases_model).filter(Clases_model.id_clase == id).first()
        if not clase:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ninguna clase con ese id")

        clase.nombre_clase = data.nombre_clase
        clase.packs_id = data.packs_id

        self.db.commit()
        return JSONResponse(status_code=200, content={"message": "Se ha actualizado la clase"})


    # BORRAR UNA CLASE
    def borrar_clase(self, id: int):
        clase = self.db.query(Clases_model).filter(Clases_model.id_clase == id).first()
        if not clase:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ninguna clase con ese id")
        self.db.query(Clases_model).filter(Clases_model.id_clase == id).delete()
        self.db.commit()
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado la clase"})
