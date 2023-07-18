from sqlalchemy.exc import SQLAlchemyError
from models.profesor_clasesModel import Profesor_clases_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from models.profesoresModel import Profesores_model
from models.clasesModel import Clases_model
from models.nivelesModel import Niveles_model


class Profesor_clases_services:
    def __init__(self) -> None:
        self.db = Session()
        #db para que cada vez que se ejecute ese servicio se envíe una sesión a la base de datos
        #ya puedo acceder a la base de datos desde otros métodos

# # Realiza la consulta
# result = session.query(Clase.nombre_baile, Nivel.nombre_nivel)\
#     .join(ProfesorBaile, Baile.id_baile == ProfesorBaile.baile_id)\
#     .join(Nivel, Nivel.id_nivel == ProfesorBaile.nivel)\
#     .filter(ProfesorBaile.baile_id == 3)\
#     .group_by(Nivel.nombre_nivel)\
#     .all()

# # Imprime los resultados
# for nombre_baile, nombre_nivel in result:
#     print(nombre_baile, nombre_nivel)


    # CONSULTAR CLASES DE UN PROFESOR
    def consultar_niveles_de_clases(self, id):
        try:
            result = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.profesor_id == id).first()
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
            nuevo_profesor = Profesor_clases_model(**data.dict())
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
            profesor = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.nombre_profesor == nombre).first()
            if not profesor:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")

            profesor.nombre_profesor = data.nombre_profesor
            profesor.apellido_profesor = data.apellido_profesor
            profesor.email_profesor = data.email_profesor
            self.db.commit()

            return {"message": "Profesor actualizado correctamente"}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # BORRAR UN PROFESOR
    def borrar_profesor(self, nombre: str):
        try:
            profesor = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.nombre_profesor == nombre).first()
            if not profesor:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún profesor con ese nombre")
            self.db.query(Profesor_clases_model).filter(Profesor_clases_model.nombre_profesor == nombre).delete()
            self.db.commit()
            return
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))