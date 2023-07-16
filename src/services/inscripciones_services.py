from fastapi import HTTPException, status
from models.incripcionesModel import Inscripciones_model
from config.db import Session


class Inscripciones_services:
    #SESION
    def __init__(self):
        self.db = Session()
        
    #CONSULTAR TODAS LAS INSCRIPCIONES
    def consultar_inscripciones(self):
        return  self.db.query(Inscripciones_model).all()
    
    #CONSULTAR UNA INSCRIPCION
    def consultar_una_inscripcion(self, id):
        return self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripciones == id).first()
    
    #CREAR UNA NUEVA INSCRIPCION
    def crear_inscripcion(self):
        return
    
    #EDITAR UNA INSCRIPCION
    def editar_inscripcion(self, data):
        return
    
    
    
            
        