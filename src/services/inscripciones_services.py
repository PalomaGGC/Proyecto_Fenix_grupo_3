from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from models.alumnosModel import Alumnos_model
from models.incripcionesModel import Inscripciones_model
from dateutil.relativedelta import relativedelta
from config.db import Session
from sqlalchemy import and_, text
from services.profesor_clases_services import Profesor_clases_services
from fastapi.encoders import jsonable_encoder


class Inscripciones_services:
    # SESION
    def __init__(self):
        self.db = Session()


    # CONSULTAR TODAS LAS INSCRIPCIONES
    def consultar_inscripciones(self):
        result = self.db.query(Inscripciones_model).all()
        if not result:
        # Si no se encuentran alumnos, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aún no hay inscripciones")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UNA INSCRIPCIÓN POR ID
    def consultar_una_inscripcion(self, id):
        result = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No existe ninguna inscripción con ese id')
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR INSCRIPCIONES PAGADAS POR ID ALUMNO
    def consultar_inscripciones_pagadas(self, id, bolean):
        result =  self.db.query(Inscripciones_model).filter(and_(Inscripciones_model.alumno_id == id, Inscripciones_model.pagada == str(bolean))).all()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No existe ninguna inscripción con ese id de alumno')
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR CUÁNTAS VECES ESTÁ INSCRITO UN ALUMNO AL MISMO PACK
    def repeticiones_pack(self, id_alumno, id_clase_profesor):
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
        return JSONResponse(status_code=200, content=jsonable_encoder(results))

    # CONSULTAR LA INFORMACIÓN DEL PACK AL QUE SE QUIERE INSCRIBIR EL ALUMNO
    def datos_pack(self, id):
        query = f"""SELECT p.id_pack, p.nombre_pack, p.precio_pack, p.primer_descuento, p.segundo_descuento
                    FROM profesores_clases AS pc
                    JOIN clases AS c ON c.id_clase = pc.clase_id
                    JOIN packs AS p ON p.id_pack = c.packs_id
                    WHERE pc.id_clase_profesor = {id} """

        result = self.db.execute(text(query)).fetchall()
        if result:
            result = [{"id_pack":data[0], "nombre_pack":data[1], "precio_pack":data[2], "primer_descuento":data[3], "segundo_descuento":data[4]} for data in result]
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CREAR UNA NUEVA INSCRIPCIÓN
    def crear_inscripcion(self, data):
        alumno = self.db.query(Alumnos_model).filter(Alumnos_model.id_alumno == data.alumno_id).first()

        if not alumno:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no existe ningún alumno con este id")

        packs_repeticiones = self.repeticiones_pack(data.alumno_id, data.profesor_clase_id)
        data_pack = self.datos_pack(data.profesor_clase_id)
        num_veces_inscrito = packs_repeticiones[0]["repeticiones"]
        primer_descuento = data_pack[0]["primer_descuento"]
        segundo_descuento = data_pack[0]["segundo_descuento"]
        precio_pack = data_pack[0]["precio_pack"]
        descuento_familiar = alumno.descuento_familiar
        fecha_inscripcion = data.fecha_inscripcion


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
            fecha_inscripcion=fecha_inscripcion, #Fecha actual
            fecha_fin=fecha_inscripcion + relativedelta(months=1)
            #Con relativedelta(months=1) le sumo 1 mes automaticamente
        )

        self.db.add(nueva_inscripcion)  # Agrega la nueva inscripción a la sesión
        self.db.commit()  # Confirma los cambios en la base de datos
        self.db.close()
        return JSONResponse(status_code=201, content={"message": "Se ha registrado un nueva inscripción"})


    # EDITAR UNA INSCRIPCIÓN
    def editar_inscripcion(self, id, data):
        inscripcion = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).first()
        if not inscripcion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="inscripcion no encontrada")

        inscripcion.precio_clase=data.precio_clase,
        inscripcion.descuento_inscripcion=data.descuento_inscripcion,
        inscripcion.descuento_familiar = data.descuento_familiar,
        inscripcion.precio_con_descuento=data.precio_con_descuento,
        inscripcion.pagada = data.pagada
        self.db.commit()
        return JSONResponse(status_code=200, content={"message": "Se ha modificado la inscripción"})


    # ELIMINAR UNA INSCRIPCIÓN
    def eliminar_inscripcion(self,id):
        inscripcion = self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).first()
        if not inscripcion:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inscripción no encontrada")

        self.db.query(Inscripciones_model).filter(Inscripciones_model.id_inscripcion == id).delete()
        self.db.commit()
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado la inscripción"})
