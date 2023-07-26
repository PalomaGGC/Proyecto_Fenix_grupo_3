from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.alumnosModel import Alumnos_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from logger import Logs




class Alumnos_services:
    def __init__(self):
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = Session()
        #ya puedo acceder a la base de datos desde otros métodos
        self.logger= Logs()

    # CONSULTAR TODOS LOS ALUMNOS
    def consultar_alumnos(self):
        result = self.db.query(Alumnos_model).all()
        self.logger.debug('Consultando todos los alumnos')
        #obtengo todos los datos Alumnos_model y los guardo en la variable result
        if not result:
            self.logger.warning('No se encontraron alumnos')
        # Si no se encuentran alumnos, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message":"Aún no hay alumnos"}) 
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UN ALUMNO POR ID
    def consultar_alumno(self, id):
        self.logger.debug(f'Consultando alumno con id: {id}')
        result = self.db.query(Alumnos_model).filter(Alumnos_model.id_alumno == id).first()
        # obtengo los datos de el alumno que quiero consultar filtrando por id,
        # obtengo los del primero que encuentre y los guardo en la variable result
        if not result:
            self.logger.warning('No se encontró el alumno')
            # Si no se encuentra el alumno, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message':'No existe ningún alumno con ese id'})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # AGREGAR UN NUEVO ALUMNO
    def agregar_alumno(self, data):
        alumno = self.db.query(Alumnos_model).filter(Alumnos_model.id_alumno == data.id_alumno).first()

        if alumno:
            self.logger.warning('El alumno ya existe con este id')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ya existe un alumno con este id")

        nuevo_alumno = Alumnos_model(**data.dict())
        #Le envío el nuevo alumno
        self.db.add(nuevo_alumno)
        #Hago el commit para que se actualice
        self.db.commit()
        self.logger.info("Se ha registrado un nuevo alumno")  # Log the event
        return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo alumno"})


    # EDITAR UN ALUMNO
    def editar_alumno(self, id: str, data):
        alumno = self.db.query(Alumnos_model).filter(Alumnos_model.id_alumno == id).first()

        if not alumno:
            self.logger.warning('No se encontró el alumno para editar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún alumno con ese id")

        alumno.nombre_alumno = data.nombre_alumno
        alumno.apellido_alumno = data.apellido_alumno
        alumno.edad_alumno = data.edad_alumno
        alumno.email_alumno = data.email_alumno
        alumno.telefono_alumno = data.telefono_alumno
        alumno.descuento_familiar = data.descuento_familiar

        self.db.commit()
        self.logger.info('Se ha modificado el alumno')
        return JSONResponse(status_code=200, content={"message": "Se ha modificado el alumno"})


    # BORRAR UN ALUMNO
    def borrar_alumno(self, id: str):
        alumno = self.db.query(Alumnos_model).filter(Alumnos_model.id_alumno == id).first()

        if not alumno:
            self.logger.warning('No se encontró el alumno para borrar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún alumno con ese id")

        self.db.query(Alumnos_model).filter(Alumnos_model.id_alumno == id).delete()
        self.db.commit()
        self.logger.info('Se ha eliminado el alumno') 
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado el alumno"})
