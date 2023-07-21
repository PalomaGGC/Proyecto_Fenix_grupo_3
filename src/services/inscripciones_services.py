
from fastapi import HTTPException, status
from sqlalchemy import func
from models.alumnosModel import Alumnos_model
from models.incripcionesModel import Inscripciones_model
from config.db import Session
from models.packsModel import Packs_model
from models.clasesModel import Clases_model
from models.profesor_clasesModel import Profesor_clases_model
from sqlalchemy import text



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
    def consultar_pack(self, id_alumno, id_clase_profesor):
        query = f"""SELECT nombre_pack, precio_pack, COUNT(nombre_pack) AS repeticiones
                    FROM inscripciones AS i
                    JOIN profesores_clases AS pc
                    ON pc.id_profesor_clase = i.profesor_clase_id
                    JOIN clases AS c
                    ON c.id_clase = pc.clase_id
                    JOIN packs AS p
                    ON p.id_pack = c.packs_id
                    WHERE i.alumno_id = {id_alumno} AND nombre_pack IN ( 
                        SELECT nombre_pack
                        FROM profesores_clases
                        JOIN clases 
                        ON clases.id_clase = profesores_clases.clase_id
                        JOIN packs 
                        ON packs.id_pack = clases.packs_id
                        WHERE profesores_clases.id_profesor_clase = {id_clase_profesor}
                    )
                    GROUP BY nombre_pack"""
                    # La primera consulta recibe el id del alumno que se esta incribiendo a 
                    # una nueva clase, en el WHERE genero una sub consulta para obtener el 
                    # nombre del pack segun el id de la tabla clase_profesor...
                    # 
                    # #
                    # la subconsulta recibe el id de Profesores_clases hago un join -
                    # para con la tabla clases y despues un join a la tabla Packs... -
                    # de la tabla packs obtengo el nombre de packs para saber a que - 
                    # packs se esta incribiendo el alumno y verificar si ya estaba inscrito -
                    # a este mismo packs
                    
        results = self.db.execute(text(query)).fetchall()
        return  results
    
    
    
    
    #CREAR UNA NUEVA INSCRIPCION
    def crear_inscripcion(self, data):
        
        dataPack = self.consultar_pack(data.alumno_id, data.profesor_clase_id)
        num_veces_inscrito = dataPack[0][2]
        precio_pack = dataPack[0][1]
        
        # INSERT INTO inscripciones (profesor_clase_id, alumno_id, precio_clase,descuento_inscripcion, precio_con_descuento, estado_inscripcion) VALUES (4,2,'35',0.5,'17.5','activo')
        
        if(num_veces_inscrito == 0):
            precio_con_descuento = precio_pack
            print("no descuento")
        elif (num_veces_inscrito == 1):
            precio_con_descuento = precio_pack * 0.5
            print("descuento del 50%")
        else:
            precio_con_descuento = precio_pack * 0.25
            print("descuento del 75%")
            
        print(dataPack)
        print(precio_con_descuento)
        
        
            
        return "todo ok"
        
    
    #EDITAR UNA INSCRIPCION
    def editar_inscripcion(self, data):
        return
    
    
    
    
            
        