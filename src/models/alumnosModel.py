from sqlalchemy import Boolean, Float, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine
from config.db import Base




class Alumno(Base):

    #creo el modelo de la tabla
    __tablename__ = "alumnos"
    id_alumno = Column(Integer, primary_key=True,  autoincrement=True)
    nombre_alumno = Column(String(100))
    apellido_alumno = Column(String(100))
    edad_alumno = Column(String(5))
    nie_alumno = Column(String(10))
    telefono_alumno = Column(String(5))
    email_alumno = Column(String(100))
    descuento_familiar = Column(Float, default=0.0)


    #creo la tabla en la base de datos
    #meta.create_all(engine)