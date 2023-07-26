from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import text
from models.profesor_clasesModel import Profesor_clases_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from models.profesor_clasesModel import Profesor_clases_model
from logger import Logs

class Profesor_clases_services:
    def __init__(self) -> None:
        self.db = Session()
        #db para que cada vez que se ejecute ese servicio se envíe una sesión a la base de datos
        #ya puedo acceder a la base de datos desde otros métodos
        self.logger= Logs()


    # CONSULTAR TODAS LAS RELACIONES 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    def consultar_profesor_clases(self):
        result = self.db.query(Profesor_clases_model).all()
        self.logger.debug('Consultando todos los profesores por clases')
        # Obtengo todos los datos Profesor_clases_model y los guardo en la variable result.
        if not result:
            self.logger.warning('No se encontraron profesores por clases')
        # Si no se encuentra la relación de profesor clase y nivel, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aún no hay relaciones 'profesor - clase - nivel' ") 
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    def consultar_profesor_clase_nivel_por_id(self, id):
        result = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.id_clase_profesor == id).first()
        self.logger.debug(f'Consultando profesor por clases y nivel por id')
        # Obtengo los datos del profesor que quiero consultar filtrando por nombre.
        # Obtengo los del primero que encuentre y los guardo en la variable result.
        if not result:
            self.logger.warning('No se encontró el profesor por clases y nivel')
            # Si no se encuentra el alumno, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ninguna relación 'profesor - clase - nivel' con ese id")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    def consultar_profesor_clase_nivel_por_nombre_clase(self, nombre):
        query = f"""SELECT profesores_clases.id_clase_profesor, clases.nombre_clase, niveles.nombre_nivel, profesores.nombre_profesor
                    FROM profesores_clases
                    JOIN clases
                    ON clases.id_clase = profesores_clases.clase_id
                    JOIN niveles
                    ON niveles.id_nivel = profesores_clases.nivel_id
                    JOIN profesores
                    ON profesores.id_profesor = profesores_clases.profesor_id
                    WHERE clases.nombre_clase = '{nombre}'"""

        result = self.db.execute(text(query)).fetchall()
        result_dicts = [{'id':row[0],  'nombre de clase':row[1],  'nivel':row[2], 'profesor':row[3]}  for row in result]

        if not result:
             self.logger.warning('No se encontró el profesor por clases y nivel')
                 # Si no se encuentra la relación que buscamos, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error.
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relación 'profesor - clase -nivel ' no encontrada")

        return JSONResponse(status_code=200, content=jsonable_encoder(result_dicts))


        # CONSULTAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL' POR ID_CLASE_PROFESOR
    def consultar_profesor_clase_nivel_por_nombre_profesor(self, nombre):
        query = f"""SELECT profesores.nombre_profesor, clases.nombre_clase, niveles.nombre_nivel
                FROM profesores_clases
                JOIN clases
                ON clases.id_clase = profesores_clases.clase_id
                JOIN niveles
                ON niveles.id_nivel = profesores_clases.nivel_id
                JOIN profesores
                ON profesores.id_profesor = profesores_clases.profesor_id
                WHERE profesores.nombre_profesor = '{nombre}'"""

        result = self.db.execute(text(query)).fetchall()
        result_dicts = [{'profesor':row[0],  'nombre de clase':row[1],  'nivel':row[2]}  for row in result]

        if not result:
            self.logger.warning('No se encontró el profesor por clases y nivel')
                 # Si no se encuentra el profesor, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error.
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relación 'profesor - clase -nivel ' no encontrada")

        return JSONResponse(status_code=200, content=jsonable_encoder(result_dicts))


    # AGREGAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL'
    def agregar_profesor_clase_nivel(self, data):
        profesor_clase = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.id_clase_profesor == data.id_clase_profesor).first()
        if profesor_clase:
            self.logger.warning('El profesor por clases y nivel ya existe con este id')
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe una relación 'profesor - clase -nivel' con este id")
        nuevo_profesor_clase = Profesor_clases_model(**data.dict())
        #Le envío el nuevo profesor
        self.db.add(nuevo_profesor_clase)
        #Hago el commit para que se actualice
        self.db.commit()
        self.logger.info("Se ha registrado un nuevo profesor por clases y nivel")
        return JSONResponse(status_code=201, content={"message": "Se ha registrado una nueva relación 'profesor - clase -nivel' "})


    # EDITAR UNA RELACIÓN 'PROFESOR - CLASE - NIVEL'
    def editar_profesor_clase_nivel(self, id: int, data):
        profesor_clase = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.id_clase_profesor == id).first()
        if not profesor_clase:
            self.logger.warning('No se encontró el profesor por clases y nivel para editar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ninguna relación 'profesor - clase -nivel' con ese id")

        profesor_clase.clase_id = data.clase_id
        profesor_clase.profesor_id = data.profesor_id
        profesor_clase.nivel_id = data.nivel_id

        self.db.commit()
        self.logger.info('Se ha modificado el profesor por clases y nivel')
        return JSONResponse(status_code=200, content={"message": "Relación 'profesor - clase -nivel' actualizada correctamente"})


    # BORRAR UNA RELACIÓN RELACIÓN 'PROFESOR - CLASE - NIVEL'
    def borrar_profesor_clase_nivel(self, id: int):
        profesor_clase = self.db.query(Profesor_clases_model).filter(Profesor_clases_model.id_clase_profesor == id).first()

        if not profesor_clase:
            self.logger.warning('No se encontró el profesor por clases y nivel para borrar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ninguna relación 'profesor - clase -nivel' con ese id")

        self.db.query(Profesor_clases_model).filter(Profesor_clases_model.id_clase_profesor == id).delete()
        self.db.commit()
        self.logger.info('Se ha eliminado el profesor por clases y nivel')
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado la relación 'profesor - clase -nivel'"})

