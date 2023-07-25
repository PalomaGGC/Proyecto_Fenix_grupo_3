from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.nivelesModel import Niveles_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from logger import Logs

class Niveles_services:
    def __init__(self) -> None:
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = Session()
        #ya puedo acceder a la base de datos desde otros métodos
        self.logger= Logs()


    # CONSULTAR TODOS LOS NIVELES
    def consultar_niveles(self):
        result = self.db.query(Niveles_model).all()
        self.logger.debug('Consultando todos los niveles')
        #obtengo todos los datos Niveles_model y los guardo en la variable result
        if not result:
            self.logger.warning('No se encontraron niveles')
        # Si no se encuentran alumnos, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aún no hay niveles")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UN NIVEL
    def consultar_nivel(self, nombre):
        result = self.db.query(Niveles_model).filter(Niveles_model.nombre_nivel == nombre).first()
        self.logger.debug(f'Consultando nivel por nombre')
        #obtengo los datos de el nivel que quiero consultar filtrando por nombre, 
        # obtengo los del primero que encuentre y los guardo en la variable result
        if not result:
            self.logger.warning('No se encontró el nivel')
            # Si no se encuentra el nivel, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún nivel con ese nombre")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # AGREGAR UN NIVEL
    def agregar_nivel(self, data):
        nivel = self.db.query(Niveles_model).filter(Niveles_model.nombre_nivel == data.nombre_nivel).first()
        if nivel:
            self.logger.warning('El nivel ya existe con este nombre')
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe un nivel con este nombre")

        nuevo_nivel = Niveles_model(**data.dict())
        #Le envío el nuevo nivel
        self.db.add(nuevo_nivel)
        #Hago el commit para que se actualice
        self.db.commit()
        self.logger.info("Se ha registrado un nuevo nivel")
        return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo nivel"})


    # EDITAR UN NIVEL
    def editar_nivel(self, nombre: str, data):
        nivel = self.db.query(Niveles_model).filter(Niveles_model.nombre_nivel == nombre).first()
        if not nivel:
            self.logger.warning('No se encontró el nivel para editar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún alumno con ese nombre")

        nivel.nombre_nivel = data.nombre_nivel
        self.db.commit()
        self.logger.info('Se ha modificado el nivel')
        return JSONResponse(status_code=200, content={"message": "Se ha modificado el nivel"})

