from sqlalchemy.exc import SQLAlchemyError
from models.nivelesModel import Niveles_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session


class Niveles_services:
    def __init__(self) -> None:
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = Session()
        #ya puedo acceder a la base de datos desde otros métodos

    # CONSULTAR TODOS LOS NIVELES
    def consultar_niveles(self):
        try:
            result = self.db.query(Niveles_model).all()
            #obtengo todos los datos Niveles_model y los guardo en la variable result
            return result
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, se lanza una excepción HTTP con el código de estado 500 y el detalle del error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # CONSULTAR UN NIVEL
    def consultar_nivel(self, nombre):
        try:
            result = self.db.query(Niveles_model).filter(Niveles_model.nombre_nivel == nombre).first()
            #obtengo los datos de el nivel que quiero consultar filtrando por nombre, 
            # obtengo los del primero que encuentre y los guardo en la variable result
            if not result:
                # Si no se encuentra el nivel, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nivel no encontrado")
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # AGREGAR UN NIVEL
    def agregar_nivel(self, data):
        try:
            nivel = self.db.query(Niveles_model).filter(Niveles_model.nombre_nivel == data.nombre_nivel).first()
            print(data)
            if nivel:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ya existe un nivel con este nombre")

            nuevo_nivel = Niveles_model(**data.model_dump())
            #Le envío el nuevo nivel
            self.db.add(nuevo_nivel)
            #Hago el commit para que se actualice
            self.db.commit()
            return f"Se agregó el nivel {nuevo_nivel} correctamente"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # EDITAR UN NIVEL
    def editar_nivel(self, nombre: str, data):
        try:
            nivel = self.db.query(Niveles_model).filter(Niveles_model.nombre_nivel == nombre).first()
            if not nivel:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nivel no encontrado")

            nivel.nombre_nivel = data.nombre_nivel
            
            self.db.commit()
            return {"message": "Nivel actualizado correctamente"}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

   