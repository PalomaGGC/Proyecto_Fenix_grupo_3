from sqlalchemy.exc import SQLAlchemyError
from models.alumnosModel import Alumnos_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session


class Alumnos_services:
    def __init__(self) -> None:
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = Session()
        #ya puedo acceder a la base de datos desde otros métodos

    # CONSULTAR TODOS LOS ALUMNOS
    def consultar_alumnos(self):
        try:
            result = self.db.query(Alumnos_model).all()
            #obtengo todos los datos Alumnos_model y los guardo en la variable result
            return result
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, se lanza una excepción HTTP con el código de estado 500 y el detalle del error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # CONSULTAR UN ALUMNO
    def consultar_alumno(self, nie):
        try:
            result = self.db.query(Alumnos_model).filter(Alumnos_model.nie_alumno == nie).first()
            #obtengo los datos de el alumno que quiero consultar filtrando por nie, 
            # obtengo los del primero que encuentre y los guardo en la variable result
            if not result:
                # Si no se encuentra el alumno, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
                raise HTTPException(status_code=status.HTTP_204_NOT_FOUND, detail="Alumno no encontrado")
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # AGREGAR UN ALUMNO
    def agregar_alumno(self, data):
        try:
            alumno = self.db.query(Alumnos_model).filter(Alumnos_model.nie_alumno == data.nie_alumno).first()
            print(data)
            if alumno:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ya existe un alumno con este nie")

            nuevo_alumno = Alumnos_model(**data.model_dump())
            #Le envío la nueva película
            self.db.add(nuevo_alumno)
            #Hago el commit para que se actualice
            self.db.commit()
            return f"Se agregó el alumno {nuevo_alumno} correctamente"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # EDITAR UN ALUMNO
    def editar_alumno(self, nie: str, data):
        try:
            alumno = self.db.query(Alumnos_model).filter(Alumnos_model.nie_alumno == nie).first()
            if not alumno:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno no encontrado")

            alumno.nombre_alumno = data.nombre_alumno
            alumno.apellido_alumno = data.apellido_alumno
            alumno.edad_alumno = data.edad_alumno
            alumno.nie_alumno = data.nie_alumno
            alumno.email_alumno = data.email_alumno
            alumno.telefono_alumno = data.telefono_alumno
            alumno.descuento_familiar = data.descuento_familiar

            self.db.commit()
            return {"message": "Alumno actualizado correctamente"}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # BORRAR UN ALUMNO
    def borrar_alumno(self, nie: str):
        try:
            alumno = self.db.query(Alumnos_model).filter(Alumnos_model.nie_alumno == nie).first()
            if not alumno:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún alumno con ese nie")
            self.db.query(Alumnos_model).filter(Alumnos_model.nie_alumno == nie).delete()
            self.db.commit()
            return
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))