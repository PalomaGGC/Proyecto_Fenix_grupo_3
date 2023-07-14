from fastapi import HTTPException, status
from schemas.alumnos import Alumnos
from config.db import conexion
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.alumnosModel import Alumno as AlumnoModel
from sqlalchemy.orm import Session



class Alumnos_services:
    def __init__(self, db: Session) -> None: #db para que cada vez que se ejecute ese servicio se envíe una sesión a la base de datos
        self.db = db
        #ya puedo acceder a la base de datos desde otros métodos

    #TODOS LOS ALUMNOS
    def consultar_alumnos(self):
        result = self.db.query(AlumnoModel).all()
        #obtengo todos los datos AlumnoModel y los guardo en la variable result
        return result

    # def consultar_alumnos(self):
    #     try:
    #         # Extraer todos los registros de la tabla "alumnos"
    #         query = Alumno.select()
    #         result = conexion.execute(query).fetchall()

    #         # Convertir los resultados a una lista de alumnos
    #         alumnos = []
    #         for item in result:
    #             alumno = {
    #                 "nombre_alumno": item[1],
    #                 "apellido_alumno": item[2],
    #                 "edad_alumno": item[3],
    #                 "nie_alumno": item[4],
    #                 "telefono_alumno": item[5],
    #                 "email_alumno": item[6],
    #                 "descuento_familiar": item[7]
    #             }
    #             alumnos.append(alumno)

    #         # Retornar la lista de alumnos en formato JSON
    #         return JSONResponse(status_code=status.HTTP_200_OK, content=alumnos)
    #     except SQLAlchemyError as e:
    #         return {"error": str(e)}



    #UN ALUMNO
    # def consultar_alumno(self, nie):
    #     try:
    #         # Buscar el alumno por su NIE en la base de datos
    #         query = alumnos.select().where(tabla_alumnos.c.nie_alumno == nie)
    #         result = conexion.execute(query).fetchone()

    #         # Verificar si se encontró un alumno con el NIE especificado
    #         if result is None:
    #             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno no encontrado")


    #         # Crear un diccionario con los datos del alumno
    #         alumno = {
    #             "nombre_alumno": result[1],
    #             "apellido_alumno": result[2],
    #             "edad_alumno": result[3],
    #             "nie_alumno": result[4],
    #             "telefono_alumno": result[5],
    #             "email_alumno": result[6],
    #             "descuento_familiar": result[7]
    #         }

    #         # Retornar el alumno en formato JSON
    #         return JSONResponse(status_code=status.HTTP_200_OK, content=alumno)
    #     except SQLAlchemyError as e:
    #         return {"error": str(e)}

    def consultar_alumno(self, nie):
        result = self.db.query(AlumnoModel).filter(AlumnoModel.nie_alumno == nie).first()
        #obtengo los datos de el alumno que quiero consultar filtrando por nie, obtengo los del primero que encuentre y los guardo en la variable result
        return result

    #AGREGAR UN ALUMNO
    def agregar_alumno(self, data):
        try:
            nuevo_alumno = AlumnoModel(**data.model_dump())
            self.db.add(nuevo_alumno)
            #Le envío la nueva película
            #Hago el commit para que se actualice
            self.db.commit()
            return f"Se agregó el alumno {nuevo_alumno} correctamente"
        except SQLAlchemyError as e:
            return {"error": str(e)}



    def editar_alumno(self, nie: str, data):
        alumno = self.db.query(AlumnoModel).filter(AlumnoModel.nie_alumno == nie).first()
        alumno.nombre_alumno = data. nombre_alumno
        alumno.apellido_alumno = data.apellido_alumno
        alumno.edad_alumno = data.edad_alumno
        alumno.nie_alumno = data.nie_alumno
        alumno.email_alumno = data.email_alumno
        alumno.telefono_alumno = data.telefono_alumno
        alumno.descuento_familiar = data.descuento_familiar
        self.db.commit()
        return

    # #EDITAR UN ALUMNO
    # def editar_alumno(self, id, data):
    #         try:
    #             # Verificar si el alumno existe en la base de datos
    #             existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.id_alumnos == id)).first()
    #             if not existe_alumno:
    #                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró ningún alumno con el ID especificado.")


    #             # Preparar los valores que se van a actualizar
    #             valores_actualizados = {
    #                 "nombre_alumno": data.nombre_alumno,
    #                 "apellido_alumno": data.apellido_alumno,
    #                 "edad_alumno": data.edad_alumno,
    #                 "nie_alumno": data.nie_alumno,
    #                 "telefono_alumno": data.telefono_alumno,
    #                 "email_alumno": data.email_alumno,
    #                 "descuento_familiar": data.descuento_familiar
    #             }


    #             # Actualizar el alumno en la base de datos
    #             query = tabla_alumnos.update().where(tabla_alumnos.c.id_alumnos == id).values(**valores_actualizados)
    #             conexion.execute(query)
    #             conexion.commit()

    #             return {"message": "Alumno actualizado correctamente."}
    #         except SQLAlchemyError as e:
    #             return {"error": str(e)}