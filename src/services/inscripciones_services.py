import datetime
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from models.incripcionesModel import Inscripciones_model
from dateutil.relativedelta import relativedelta
from config.db import Session
from sqlalchemy import and_, text
from services.alumnos_services import Alumnos_services
from services.profesor_clases_services import Profesor_clases_services


class Inscripciones_services:
    #SESION
    def __init__(self):
        self.db = Session()
        
    #CONSULTAR TODAS LAS INSCRIPCIONES
    def consultar_inscripciones(self):
        try:
            result = self.db.query(Inscripciones_model).all()
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
    #CONSULTAR UNA INSCRIPCION
    def consultar_una_inscripcion(self, id):
        try:
           result = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).first()
           if not result:
               raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="alumno no encontrado")
           return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
        
    #CONSULTAR INSCRIPCIONES PAGAS POR ID ALUMNO
    def consultar_inscripciones_pagadas(self, id, bolean):
        try:
            result =  self.db.query(Inscripciones_model).filter(and_(Inscripciones_model.alumno_id == id, Inscripciones_model.pagada == str(bolean))).all()
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
    #CONSULTO CUANTAS VECES ESTA INSCRITO AL MISMO PACK
    def repeticiones_pack(self, id_alumno, id_clase_profesor):
        try:
            #Valido que clase_profesor si existe, si no existe la clase Profesor_clases_services() retornara una exepcion
            Profesor_clases_services().consultar_profesor_clase_nivel_por_id(id_clase_profesor)
            query = f""" SELECT COUNT(nombre_pack) AS repeticiones
                        FROM inscripciones AS i
                        JOIN profesores_clases AS pc ON pc.id_clase_profesor = i.profesor_clase_id
                        JOIN clases AS c ON c.id_clase = pc.clase_id
                        JOIN packs AS p ON p.id_pack = c.packs_id
                        WHERE i.alumno_id = {id_alumno} AND nombre_pack IN
                        ( 
                            SELECT nombre_pack
                            FROM profesores_clases
                            JOIN clases ON clases.id_clase = profesores_clases.clase_id
                            JOIN packs ON packs.id_pack = clases.packs_id
                            WHERE profesores_clases.id_clase_profesor = {id_clase_profesor}
                        )
                        GROUP BY nombre_pack """
            # La primera consulta recibe el id del alumno que se esta incribiendo a 
            # una nueva clase, en el WHERE genero una sub consulta para obtener el 
            # nombre del pack segun el id de la tabla clase_profesor...
            # #
            # la subconsulta recibe el id de Profesores_clases hago un join -
            # para con la tabla clases y despues un join a la tabla Packs... -
            # de la tabla packs obtengo el nombre de packs para saber a que - 
            # packs se esta incribiendo el alumno y verificar si ya estaba inscrito -
            # a este mismo packs
            results = self.db.execute(text(query)).fetchall()
            # si hay resultado retorno un diccionario con el numero de repeticiones
            if results:
                results = [{"repeticiones":results[0][0]}]
            else:
                results = [{"repeticiones":0}]
            return  results
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
    
    def datos_pack(self, id):
        try:
            query = f"""SELECT p.id_pack, p.nombre_pack, p.precio_pack, p.primer_descuento, p.segundo_descuento
                        FROM profesores_clases AS pc
                        JOIN clases AS c ON c.id_clase = pc.clase_id
                        JOIN packs AS p ON p.id_pack = c.packs_id
                        WHERE pc.id_clase_profesor = {id} """
                        
            result = self.db.execute(text(query)).fetchall()
            if result:
                result = [{"id_pack":data[0], "nombre_pack":data[1], "precio_pack":data[2], "primer_descuento":data[3], "segundo_descuento":data[4]} for data in result]
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
  
  
  
    #CREAR UNA NUEVA INSCRIPCION
    def crear_inscripcion(self, data):
        try:
            # crear_nueva_inscripcion()
            alumno = Alumnos_services().consultar_alumno(data.alumno_id)
            packs_repeticiones = self.repeticiones_pack(data.alumno_id, data.profesor_clase_id)
            data_pack = self.datos_pack(data.profesor_clase_id)
            num_veces_inscrito = packs_repeticiones[0]["repeticiones"]
            primer_descuento = data_pack[0]["primer_descuento"]
            segundo_descuento = data_pack[0]["segundo_descuento"]
            precio_pack = data_pack[0]["precio_pack"]
            descuento_familiar = alumno.descuento_familiar

            if(num_veces_inscrito == 0):
                #Aplico el descuento correspondiente 35 - (35 * 0.1)
                precio_con_descuento = precio_pack - (precio_pack * descuento_familiar)
                #Obtengo el descuento que se utilizo 0
                descuento_aplicado = 0.0
            elif (num_veces_inscrito == 1):
                #Aplico el descuento correspondiente 35 - (35 * 0.5) = 17,50
                precio = precio_pack - ( precio_pack * primer_descuento )
                #Aplico descuento familiar 17.50 - (17,50 * 0.1) = 15,75
                precio_con_descuento = precio - (precio * descuento_familiar)
                #Obtengo el descuento que se utilizo 0.5
                descuento_aplicado = primer_descuento
            else:
                #Aplico el descuento correspondiente 35 - (35 * 0.75) = 8.75
                precio = precio_pack - ( precio_pack * segundo_descuento )
                #Aplico descuento familiar 8.75 - (8.75 * 0.1) = 7,87
                precio_con_descuento = precio - (precio * descuento_familiar)
                #Obtengo el descuento que se utilizo 0.75
                descuento_aplicado = segundo_descuento
                
            # # Creo una nueva instancia del modelo Inscripcion_model con los datos proporcionados

            nueva_inscripcion = Inscripciones_model(
                profesor_clase_id=data.profesor_clase_id,
                alumno_id=data.alumno_id,
                precio_clase=precio_pack,
                descuento_inscripcion=descuento_aplicado,
                descuento_familiar = descuento_familiar,
                precio_con_descuento=precio_con_descuento,
                pagada='true',
                fecha_inscripcion=datetime.datetime.now(), #Fecha actual
                fecha_fin=datetime.datetime.now() + relativedelta(months=1) 
                #Con relativedelta(months=1) le sumo 1 mes automaticamente
            )

            self.db.add(nueva_inscripcion)  # Agrega la nueva inscripción a la sesión
            self.db.commit()  # Confirma los cambios en la base de datos
            self.db.close()

            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Inscripción creada exitosamente"})
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
        
    
    #EDITAR UNA INSCRIPCION
    def editar_inscripcion(self, id, data):
        try:
            result = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripciones == id).first()
            if not result:
               raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="inscripcion no encontrada")
           
            result.precio_clase=data.precio_clase,
            result.descuento_inscripcion=data.descuento_inscripcion,
            result.descuento_familiar = data.descuento_familiar,
            result.precio_con_descuento=data.precio_con_descuento,
            result.estado_inscripcion = data.estado_inscripcion
            self.db.commit() 
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Inscripción editada exitosamente"})
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    
    
    #ELIMINAR UNA INSCRIPCION
    def eliminar_inscripcion(self,id):
        try:
            result = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).first()
            if not result:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="inscripcion no encontrada")
            
            self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripciones == id).delete()
            self.db.commit()
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Inscripción borrada exitosamente"})
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        return
    
    
    