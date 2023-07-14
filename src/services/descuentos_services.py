from fastapi import HTTPException, status
from models.descuentosModel import Descuento_model
from sqlalchemy.exc import SQLAlchemyError
from models.descuentosModel import Descuento_model
from config.db import Session

class Descuentos_services:
    def __init__(self):
        self.db = Session()

    #COSULTAR TODOS LOS DESCUENTOS
    def consultar_descuentos(self):
        try:
            descuentos = self.db.query(Descuento_model).all()
            return descuentos
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    #CONSULTAR UN DESCUENTO
    def consultar_un_descuento(self, id):
        try:
            descuento = self.db.query(Descuento_model).filter(Descuento_model.id_descuento == id).first()
            if not descuento:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Descuento no encontrado")
            return descuento
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    #AGREGAR UN NUEVO DESCUENTO
    def crear_descuento(self, data):
        try:
            nuevo_descuento = Descuento_model(**data.model_dump())
            self.db.add(nuevo_descuento)
            self.db.commit()
            return "{'message':'Se agrego un nuevo descuento'}"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def editar_descuento(self, id, data):
        try:
            descuento = self.db.query(Descuento_model).filter(Descuento_model.id_descuento == id).first()
            if not descuento:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Descuento no encontrado")
            descuento.tipo_descuento = data.tipo_descuento
            descuento.porcentage_descuento = data.porcentage_descuento
            self.db.commit()
            return {"message": "Descuento actualizado correctamente."}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    
    