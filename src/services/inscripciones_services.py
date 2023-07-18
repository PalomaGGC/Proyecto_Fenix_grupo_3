from fastapi import HTTPException, status
from sqlalchemy import func
from models.alumnosModel import Alumnos_model
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
        #verificar a que pack se esta inscribiendo
        pack_entrante = ""
        #verfificar si este alumno ya estaba inscrito a este mismo pack y cuantas veces
        pack_informacion = self.db.query(Inscripciones_model).join(Alumno, Alumno.id_alumno == Inscripciones_model.alumnos_id) \
    
        
        # # Realizar la consulta utilizando SQL Alchemy
        # consulta = session.query(Pack.precio_pack.label('precio'), func.count(Pack.nombre_pack).label('num_veces')) \
        #     .join(Alumnos, Alumnos.id_alumno == Inscripcion.alumno_id) \
        #     .join(ProfesorBaile, ProfesorBaile.id_profesor_baile == Inscripcion.baile_profesor_id) \
        #     .join(Bailes, Bailes.id_baile == ProfesorBaile.baile_id) \
        #     .join(Pack, Pack.id_pack == Bailes.pack_baile) \
        #     .filter(Alumnos.nombre == 'catalina') \
        #     .filter(Pack.nombre_pack == 'pack 1') \
        #     .group_by(Pack.nombre_pack)

        # # Ejecutar la consulta
        # resultados = consulta.all()
        
        
        
        #verifivar el precio de la clase
        #aplicar el descuento correspondiente
        #enviar los datos al servidor
        
        return
    
    #EDITAR UNA INSCRIPCION
    def editar_inscripcion(self, data):
        return
    
    
    
    
            
        