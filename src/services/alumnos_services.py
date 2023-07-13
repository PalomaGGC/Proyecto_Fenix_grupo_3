from fastapi import HTTPException, status
from models.alumnosModel import tabla_alumnos
from config.db import conexion
from sqlalchemy.exc import SQLAlchemyError
from schemas.alumnos import Alumnos
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.alumnosModel import Alumno as AlumnoModel


class Alumnos_services:



    #TODOS LOS ALUMNOS
    def alumnos(self):
        try:
            # Extraer todos los registros de la tabla "alumnos"
            query = tabla_alumnos.select()
            result = conexion.execute(query).fetchall()

            # Convertir los resultados a una lista de alumnos
            alumnos = []
            for item in result:
                alumno = {
                    "nombre_alumno": item[1],
                    "apellido_alumno": item[2],
                    "edad_alumno": item[3],
                    "nie_alumno": item[4],
                    "telefono_alumno": item[5],
                    "email_alumno": item[6],
                    "descuento_familiar": item[7]
                }
                alumnos.append(alumno)

            # Retornar la lista de alumnos en formato JSON
            return JSONResponse(status_code=status.HTTP_200_OK, content=alumnos)
        except SQLAlchemyError as e:
            return {"error": str(e)}






    #UN ALUMNO
    def alumno(self, nie):
        try:
            # Buscar el alumno por su NIE en la base de datos
            query = tabla_alumnos.select().where(tabla_alumnos.c.nie_alumno == nie)
            result = conexion.execute(query).fetchone()

            # Verificar si se encontró un alumno con el NIE especificado
            if result is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alumno no encontrado")


            # Crear un diccionario con los datos del alumno
            alumno = {
                "nombre_alumno": result[1],
                "apellido_alumno": result[2],
                "edad_alumno": result[3],
                "nie_alumno": result[4],
                "telefono_alumno": result[5],
                "email_alumno": result[6],
                "descuento_familiar": result[7]
            }

            # Retornar el alumno en formato JSON
            return JSONResponse(status_code=status.HTTP_200_OK, content=alumno)
        except SQLAlchemyError as e:
            return {"error": str(e)}






    #AGREGAR UN ALUMNO

    
    def insertar_alumno(self, data: Alumnos):
        nuevo_alumno = AlumnoModel(**data.model_dump())
        self.db.add(nuevo_alumno)
        #Le envío la nueva película
        self.db.commit()
        #Hago el commit para que se actualice
        return




        '''try:
        # Verificar si el NIE del alumno ya existe en la base de datos
            existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.nie_alumno == data.nie_alumno)).first()
            if existe_alumno:

                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se puede agregar el alumno. El NIE ya está registrado.")

            # Preparar los valores que se van a guardar
            nuevo_alumno = {
                "nombre_alumno": data.nombre_alumno,
                "apellido_alumno": data.apellido_alumno,
                "edad_alumno": data.edad_alumno,
                "nie_alumno": data.nie_alumno,
                "email_alumno": data.email_alumno,
                "telefono_alumno": data.telefono_alumno,
                "descuento_familiar": data.descuento_familiar
            }

            # Insertar el nuevo alumno en la base de datos
            conexion.execute(tabla_alumnos.insert().values(**nuevo_alumno))
            # Hacer un commit a la base de datos
            conexion.commit()

            return f"Se agregó el alumno {nuevo_alumno} correctamente"
        except SQLAlchemyError as e:
            return {"error": str(e)}'''
        
        
        
        
        
        
        
        
    #EDITAR UN ALUMNO
    def editar_alumno(self, id, data):
            try:
                # Verificar si el alumno existe en la base de datos
                existe_alumno = conexion.execute(tabla_alumnos.select().where(tabla_alumnos.c.id_alumnos == id)).first()
                if not existe_alumno:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró ningún alumno con el ID especificado.")
                

                # Preparar los valores que se van a actualizar
                valores_actualizados = {
                    "nombre_alumno": data.nombre_alumno,
                    "apellido_alumno": data.apellido_alumno,
                    "edad_alumno": data.edad_alumno,
                    "nie_alumno": data.nie_alumno,
                    "telefono_alumno": data.telefono_alumno,
                    "email_alumno": data.email_alumno,
                    "descuento_familiar": data.descuento_familiar
                }
                

                # Actualizar el alumno en la base de datos
                query = tabla_alumnos.update().where(tabla_alumnos.c.id_alumnos == id).values(**valores_actualizados)
                conexion.execute(query)
                conexion.commit()

                return {"message": "Alumno actualizado correctamente."}
            except SQLAlchemyError as e:
                return {"error": str(e)}