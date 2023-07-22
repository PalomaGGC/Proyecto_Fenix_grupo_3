
import json
from fastapi import HTTPException, status
from sqlalchemy import func
from models.alumnosModel import Alumnos_model
from models.incripcionesModel import Inscripciones_model
from config.db import Session
from models.packsModel import Packs_model
from models.clasesModel import Clases_model
from models.profesor_clasesModel import Profesor_clases_model
from sqlalchemy import text
from services.alumnos_services import Alumnos_services
from services.profesor_clases_services import Profesor_clases_services


class Inscripciones_services:
    #SESION
    def __init__(self):
        self.db = Session()
        
    #CONSULTAR TODAS LAS INSCRIPCIONES
    def consultar_inscripciones(self):
        return  self.db.query(Inscripciones_model).all()
    
    #CONSULTAR UNA INSCRIPCION
    def consultar_una_inscripcion(self):
        return self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripciones == id).first()
    
    #Consulto cuantas veces se a incrito al mismo pack
    def repeticiones_pack(self, id_alumno, id_clase_profesor):
         # La primera consulta recibe el id del alumno que se esta incribiendo a 
        # una nueva clase, en el WHERE genero una sub consulta para obtener el 
        # nombre del pack segun el id de la tabla clase_profesor...
        # #
        # la subconsulta recibe el id de Profesores_clases hago un join -
        # para con la tabla clases y despues un join a la tabla Packs... -
        # de la tabla packs obtengo el nombre de packs para saber a que - 
        # packs se esta incribiendo el alumno y verificar si ya estaba inscrito -
        # a este mismo packs
        query = f"""
                    SELECT COUNT(nombre_pack) AS repeticiones
                    FROM inscripciones AS i
                    JOIN profesores_clases AS pc ON pc.id_clase_profesor = i.profesor_clase_id
                    JOIN clases AS c ON c.id_clase = pc.clase_id
                    JOIN packs AS p ON p.id_pack = c.packs_id
                    WHERE i.alumno_id = {id_alumno} AND nombre_pack IN ( 
                        SELECT nombre_pack
                        FROM profesores_clases
                        JOIN clases ON clases.id_clase = profesores_clases.clase_id
                        JOIN packs ON packs.id_pack = clases.packs_id
                        WHERE profesores_clases.id_clase_profesor = {id_clase_profesor}
                    )
                    GROUP BY nombre_pack
                """
                   
        results = self.db.execute(text(query)).fetchall()
        results_dict = [{"repeticiones":results[0][0]}]
        return  results_dict
    
    
    
    def datos_pack(self, id):
        query = f"""
                    SELECT p.id_pack, p.nombre_pack, p.precio_pack, p.primer_descuento, p.segundo_descuento
                    FROM profesores_clases AS pc
                    JOIN clases AS c ON c.id_clase = pc.clase_id
                    JOIN packs AS p ON p.id_pack = c.packs_id
                    WHERE pc.id_clase_profesor = {id}
                """
        result = self.db.execute(text(query)).fetchall()     
        result_dict = [{"id_pack":data[0], "nombre_pack":data[1], "precio_pack":data[2], "primer_descuento":data[3], "segundo_descuento":data[4]} for data in result]                  
        return result_dict
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    #CREAR UNA NUEVA INSCRIPCION
    def crear_inscripcion(self, data):
        
        
        data_repeticiones= self.repeticiones_pack(data.alumno_id, data.profesor_clase_id)
        print(data_repeticiones)
        # data_pack = self.datos_pack(data.profesor_clase_id)
   
        # if data_pack:
        #     primer_descuento = data_pack[0]["primer_descuento"]
        #     segundo_descuento = data_pack[0]["segundo_descuento"]
        #     precio_pack = data_pack[0]["precio_pack"]
        # else:
        #     primer_descuento = 0
        #     segundo_descuento = 0
        #     precio_pack =0
            
            
        
        
        
        # if data_repeticiones:
        #     num_veces_inscrito = data_repeticiones[0][2]
        # else:
        #     num_veces_inscrito = 0

            
        # if(num_veces_inscrito == 0):
        #     precio_con_descuento = precio_pack
        #     descuento_aplicado = 0.0
        # elif (num_veces_inscrito == 1):
        #     precio_con_descuento = precio_pack * primer_descuento
        #     descuento_aplicado = 0.5
        # else:
        #     precio_con_descuento = precio_pack * segundo_descuento
        #     descuento_aplicado = 0.75
            
        #  # Creo una nueva instancia del modelo Inscripcion_model con los datos proporcionados
        # nueva_inscripcion = Inscripciones_model(
        #     profesor_clase_id=data.profesor_clase_id,
        #     alumno_id=data.alumno_id,
        #     precio_clase=precio_pack,
        #     descuento_inscripcion=descuento_aplicado,
        #     precio_con_descuento=precio_con_descuento,
        #     estado_inscripcion='activo'
        # )

        # self.db.add(nueva_inscripcion)  # Agrega la nueva inscripción a la sesión
        # self.db.commit()  # Confirma los cambios en la base de datos
        # self.db.close()

        return data_repeticiones
        
    
    #EDITAR UNA INSCRIPCION
    def editar_inscripcion(self, data):
        return
    
    
    
    
            
        