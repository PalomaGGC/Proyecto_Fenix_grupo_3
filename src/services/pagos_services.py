from sqlalchemy import and_, text
from sqlalchemy.exc import SQLAlchemyError
from models.pagosModel import Pagos_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from models.incripcionesModel import Inscripciones_model


class Pagos_services:
    def __init__(self):
        self.db = Session()
       

    # CONSULTAR TODOS LOS CLASSES
    def consultar_pagos(self):
        try:
            result = self.db.query(Pagos_model).all()
            #obtengo todos los datos Clases_model y los guardo en la variable result
            return result
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, se lanza una excepción HTTP con el código de estado 500 y el detalle del error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



    # CONSULTAR UN PAGO
    def consultar_pago_por_id_del_alumno(self, id):
        try:
            query = f""" SELECT p.*, i.precio_con_descuento AS monto
                        FROM pagos AS p
                        JOIN inscripciones AS i ON i.id_inscripcion = p.inscripcion_id
                        WHERE i.alumno_id = {id}"""
            results = self.db.execute(text(query)).fetchall()
            print(results)
            if not results:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pago no encontrado")
            result_dict = [{"id":item[0], "id_inscripcion":item[1],"fecha":item[2], "monto":item[3]}for item in results]
            return result_dict
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



    #CREAR UN PAGO
    def agregar_pago(self, data):
        try:
            inscripcion = self.db.query(Inscripciones_model)\
                          .filter(and_(Inscripciones_model.id_inscripcion == data.inscripcion_id, Inscripciones_model.pagada == 'false')).first()
            if inscripcion is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="404")
        
            self.agregar_pago_en_inscripcion(data.inscripcion_id)
            nuevo_pago = Pagos_model(**data.dict())         
            self.db.add(nuevo_pago)
            self.db.commit()
            return "Se agrego el pago correctamente"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
    
    
    
    #Actualizo a TRUE en la columna pagada en la tabla de inscripciones
    def agregar_pago_en_inscripcion(self, id):
        inscripcion = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).first()
        inscripcion.pagada = 'true'
        self.db.commit()
        return