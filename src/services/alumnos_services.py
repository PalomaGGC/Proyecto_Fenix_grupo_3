from sqlalchemy.exc import SQLAlchemyError
from models.alumnosModel import Alumno as AlumnoModel
from sqlalchemy.orm import Session



class Alumnos_services:
    def __init__(self, db: Session) -> None: 
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = db
        #ya puedo acceder a la base de datos desde otros métodos

    #CONSULTAR TODOS LOS ALUMNOS
    def consultar_alumnos(self):
        result = self.db.query(AlumnoModel).all()
        #obtengo todos los datos AlumnoModel y los guardo en la variable result
        return result

    #CONSULTAR UN ALUMNO
    def consultar_alumno(self, nie):
        result = self.db.query(AlumnoModel).filter(AlumnoModel.nie_alumno == nie).first()
        #obtengo los datos de el alumno que quiero consultar filtrando por nie, 
        # obtengo los del primero que encuentre y los guardo en la variable result
        return result


    #AGREGAR UN ALUMNO
    def agregar_alumno(self, data):
        try:
            nuevo_alumno = AlumnoModel(**data.model_dump())
            #Le envío la nueva película
            self.db.add(nuevo_alumno)
            #Hago el commit para que se actualice
            self.db.commit()
            return f"Se agregó el alumno {nuevo_alumno} correctamente"
        except SQLAlchemyError as e:
            return {"error": str(e)}


    #EDITAR UN ALUMNO
    def editar_alumno(self, nie: str, data):
        alumno = self.db.query(AlumnoModel).filter(AlumnoModel.nie_alumno == nie).first()
        alumno.nombre_alumno = data. nombre_alumno
        alumno.apellido_alumno = data.apellido_alumno
        alumno.edad_alumno = data.edad_alumno
        alumno.nie_alumno = data.nie_alumno
        alumno.email_alumno = data.email_alumno
        alumno.telefono_alumno = data.telefono_alumno
        alumno.descuento_familiar = data.descuento_familiar
        self.db.commit()
        return
    
   
   