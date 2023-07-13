from fastapi import HTTPException, status
from models.descuentosModel import tabla_descuentos
from config.db import conexion
from sqlalchemy.exc import SQLAlchemyError
from schemas.descuentos import Descuentos
from fastapi.responses import JSONResponse


class Descuentos_services:
    
    
    def descuentos(self):
        try:
            # Extraer todos los registros de la tabla "alumnos"
            query = tabla_descuentos.select()
            result = conexion.execute(query).fetchall()

            # Convertir los resultados a una lista de alumnos
            descuentos = []
            for item in result:
                descuento = {
                    "id_descuento": item[0],
                    "tipo_descuento": item[1],
                    "porcentage_descuento": item[2],
                }
                descuentos.append(descuento)

            # Retornar la lista de alumnos en formato JSON
            return JSONResponse(status_code=status.HTTP_200_OK, content=descuentos)
        except SQLAlchemyError as e:
            return {"error": str(e)}
 
    
    
    
    def descuento(self, id):
        try:
            # Extraer todos los registros de la tabla "alumnos"
            query = tabla_descuentos.select().where(tabla_descuentos.c.id_descuento == id)
            result = conexion.execute(query).fetchall()

            # Convertir los resultados a una lista de alumnos
            descuentos = []
            for item in result:
                descuento = {
                    "id_descuento": item[0],
                    "tipo_descuento": item[1],
                    "porcentage_descuento": item[2],
                }
                descuentos.append(descuento)

            # Retornar la lista de alumnos en formato JSON
            return JSONResponse(status_code=status.HTTP_200_OK, content=descuentos)
        except SQLAlchemyError as e:
            return {"error": str(e)}
        
    
    
    def agregar_descuento(self, data):
        try:
            # Verificar si el NIE del alumno ya existe en la base de datos
                existe_alumno = conexion.execute(tabla_descuentos.select().where(tabla_descuentos.c.tipo_descuento == data.tipo_descuento)).first()
                if existe_alumno:

                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se puede agregar el nuevo descuento con un mismo tipo de descuento ")

                # Preparar los valores que se van a guardar
                nuevo_descuento = {
                    "id_descuento": data.id_descuento,
                    "tipo_descuento": data.tipo_descuento,
                    "porcentage_descuento": data.porcentage_descuento,
                }

                # Insertar el nuevo alumno en la base de datos
                conexion.execute(tabla_descuentos.insert().values(**nuevo_descuento))
                # Hacer un commit a la base de datos
                conexion.commit()

                return f"Se agregó el nuevo descuento {nuevo_descuento} correctamente"
        except SQLAlchemyError as e:
                return {"error": str(e)}
            
            
            
            
    def editar_descuento(self, id, data):
            try:
                # Verificar si el alumno existe en la base de datos
                existe_alumno = conexion.execute(tabla_descuentos.select().where(tabla_descuentos.c.id_descuento == id)).first()
                if not existe_alumno:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontró ningún descuento con el ID especificado.")
                

                # Preparar los valores que se van a actualizar
                valores_actualizados = {
                    "id_descuento": data.id_descuento,
                    "tipo_descuento": data.tipo_descuento,
                    "porcentage_descuento": data.porcentage_descuento,
                }
                

                # Actualizar el alumno en la base de datos
<<<<<<< HEAD
                query = tabla_descuentos.update().where(tabla_descuentos.c.id_alumnos == id).values(**valores_actualizados)
                conexion.execute(query)
                conexion.commit()

                return {"message": "Alumno actualizado correctamente."}
            except SQLAlchemyError as e:
                return {"error": str(e)}
        
=======
                query = tabla_descuentos.update().where(tabla_descuentos.c.id_descuento == id).values(**valores_actualizados)
                conexion.execute(query)
                conexion.commit()

                return {"message": "descuento actualizado correctamente."}
            except SQLAlchemyError as e:
                return {"error": str(e)}
    
    
>>>>>>> e0045007b4438588e2a29781e581c50659bfeb27
    
    