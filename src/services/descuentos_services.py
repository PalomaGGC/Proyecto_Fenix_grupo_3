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
        return
    
    
    # def agregar_descuento(self):
    #      try:
    #         # Verificar si el NIE del alumno ya existe en la base de datos
    #             existe_alumno = conexion.execute(tabla_descuentos.select().where(tabla_descuentos.c.nie_alumno == data.nie_alumno)).first()
    #             if existe_alumno:

    #                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se puede agregar el alumno. El NIE ya está registrado.")

    #             # Preparar los valores que se van a guardar
    #             nuevo_alumno = {
    #                 "nombre_alumno": data.nombre_alumno,
    #                 "apellido_alumno": data.apellido_alumno,
    #                 "edad_alumno": data.edad_alumno,
    #                 "nie_alumno": data.nie_alumno,
    #                 "email_alumno": data.email_alumno,
    #                 "telefono_alumno": data.telefono_alumno,
    #                 "descuento_familiar": data.descuento_familiar
    #             }

    #             # Insertar el nuevo alumno en la base de datos
    #             conexion.execute(tabla_alumnos.insert().values(**nuevo_alumno))
    #             # Hacer un commit a la base de datos
    #             conexion.commit()

    #             return f"Se agregó el alumno {nuevo_alumno} correctamente"
    #         except SQLAlchemyError as e:
    #             return {"error": str(e)}
    
    