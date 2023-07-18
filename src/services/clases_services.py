from sqlalchemy.exc import SQLAlchemyError
from models.clasesModel import Clases_model
from models.packsModel import Packs_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session


class Clases_services:
    def __init__(self):
        self.db = Session()
       

    # CONSULTAR TODOS LOS CLASSES
    def consultar_clases(self):
        try:
            result = self.db.query(Clases_model).all()
            #obtengo todos los datos Clases_model y los guardo en la variable result
            return result
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, se lanza una excepción HTTP con el código de estado 500 y el detalle del error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # CONSULTAR UN CLASE
    def consultar_clase_por_id(self, id):
        try:
            result = self.db.query(Clases_model).filter(Clases_model.id_clase == id).first()
            if not result:
                raise HTTPException(status_code=status.HTTP_204_NOT_FOUND, detail="Clase no encontrado")
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # AGREGAR UN CLASE
    def agregar_clase(self, data):
        try:
            clase = self.db.query(Clases_model).filter(Clases_model.nombre_clase == data.nombre_clase).first()
            print(data)
            if clase:
               raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ya existe un clase con este nombre")
            nuevo_clase = Clases_model(**data.dict())           
            self.db.add(nuevo_clase)
            self.db.commit()
            return f"Se agregó el clase {nuevo_clase} correctamente"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # EDITAR UN CLASE
    def editar_clase(self, id: int, data):
        try:
            clase = self.db.query(Clases_model).filter(Clases_model.id_clase == id).first()
            if not clase:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="clase no encontrado")

            clase.nombre_clase = data.nombre_clase
            clase.packs_id = data.packs_id
     
            self.db.commit()
            return {"message": "clase actualizado correctamente"}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # BORRAR UN CLASE
    def borrar_clase(self, id: int):
        try:
            clase = self.db.query(Clases_model).filter(Clases_model.id_clase == id).first()
            if not clase:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún clase con ese id")
            self.db.query(Clases_model).filter(Clases_model.id_clase == id).delete()
            self.db.commit()
            return
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)