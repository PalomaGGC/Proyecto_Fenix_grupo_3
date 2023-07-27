from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.profesoresModel import Profesores_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from logger import Logs

class Profesores_services:
    def __init__(self) -> None:
        self.db = Session()
        #db para que cada vez que se ejecute ese servicio se envíe una sesión a la base de datos
        #ya puedo acceder a la base de datos desde otros métodos
        self.logger= Logs()


    # CONSULTAR TODOS LOS PROFESORES
    def consultar_profesores(self):
        result = self.db.query(Profesores_model).all()
        self.logger.debug('Consultando todos los profesores')
        # Obtengo todos los datos Profesores_model y los guardo en la variable result.
        if not result:
            self.logger.warning('No se encontraron profesores')
        # Si no se encuentran profesores, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aún no hay profesores")
        return  JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UN PROFESOR
    def consultar_profesor(self, nombre):
        result = self.db.query(Profesores_model).filter(Profesores_model.nombre_profesor == nombre).first()
        self.logger.debug(f'Consultando profesor por id')
         # Obtengo los datos del profesor que quiero consultar filtrando por nombre.
         # Obtengo los del primero que encuentre y los guardo en la variable result.
        if not result:
            self.logger.warning('No se encontró el profesor')
            # Si no se encuentra el profesor, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error.
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # AGREGAR UN PROFESOR
    def agregar_profesor(self, data):
        profesor = self.db.query(Profesores_model).filter(Profesores_model.nombre_profesor  == data.nombre_profesor).first()
        if profesor:
            self.logger.warning('El profesor ya existe con este id')
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe un profesor con este nombre")

        nuevo_profesor = Profesores_model(**data.dict())
        #Le envío el nuevo profesor
        self.db.add(nuevo_profesor)
         #Hago el commit para que se actualice
        self.db.commit()
        self.logger.info("Se ha registrado un nuevo profesor")
        return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo profesor"})


    # EDITAR UN PROFESOR
    def editar_profesor(self, nombre: str, data):
        profesor = self.db.query(Profesores_model).filter(Profesores_model.nombre_profesor == nombre).first()
        if not profesor:
            self.logger.warning('No se encontró el profesor para editar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message':'No existe ningún profesor con ese nombre'})

        profesor.nombre_profesor = data.nombre_profesor
        profesor.apellido_profesor = data.apellido_profesor
        profesor.email_profesor = data.email_profesor
        self.db.commit()
        self.logger.info('Se ha modificado el profesor')
        return JSONResponse(status_code=200, content={"message": "Se ha modificado el profesor"})


    # BORRAR UN PROFESOR
    def borrar_profesor(self, nombre: str):
        profesor = self.db.query(Profesores_model).filter(Profesores_model.nombre_profesor == nombre).first()
        if not profesor:
            self.logger.warning('No se encontró el profesor para borrar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún profesor con ese nombre")
        self.db.query(Profesores_model).filter(Profesores_model.nombre_profesor == nombre).delete()
        self.db.commit()
        self.logger.info('Se ha eliminado el profesor')
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado el profesor"})


