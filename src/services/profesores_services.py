from sqlalchemy.exc import SQLAlchemyError
from models.profesoresModel import Profesores as ProfesorModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


class Profesores_services:
    def __init__(self, db: Session) -> None:
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = db
        #ya puedo acceder a la base de datos desde otros métodos

    # CONSULTAR TODOS LOS PROFESORES
    def consultar_profesores(self):
        try:
            result = self.db.query(ProfesorModel).all()
            # Obtengo todos los datos ProfesorModel y los guardo en la variable result.
            return result
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, se lanza una excepción HTTP con el código de estado 500 y el detalle del error.
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # CONSULTAR UN PROFESOR
    def consultar_profesor(self, nombre):
        try:
            result = self.db.query(ProfesorModel).filter(ProfesorModel.nombre_profesor == nombre).first()
            # Obtengo los datos del profesor que quiero consultar filtrando por nombre.
            # Obtengo los del primero que encuentre y los guardo en la variable result.
            if not result:
                # Si no se encuentra el profesor, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error.
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # AGREGAR UN PROFESOR
    def agregar_profesor(self, data):
        try:
            nuevo_profesor = ProfesorModel(**data.model_dump())
            #Le envío el nuevo profesor
            self.db.add(nuevo_profesor)
            #Hago el commit para que se actualice
            self.db.commit()
            return f"Se agregó el profesor {nuevo_profesor} correctamente"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # EDITAR UN PROFESOR
    def editar_profesor(self, nombre: str, data):
        try:
            profesor = self.db.query(ProfesorModel).filter(ProfesorModel.nombre_profesor == nombre).first()
            if not profesor:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")

            profesor.nombre_profesor = data.nombre_profesor
            profesor.apellido_profesor = data.apellido_profesor
            profesor.email_profesor = data.email_profesor
            self.db.commit()

            return {"message": "Profesor actualizado correctamente"}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
