from sqlalchemy import Float, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base

#MODELO DE LA TABLA
class Alumno(Base):
    __tablename__ = "alumnos"
    id_alumno = Column(Integer, primary_key=True,  autoincrement=True)
    nombre_alumno = Column(String(100))
    apellido_alumno = Column(String(100))
    edad_alumno = Column(String(5))
    nie_alumno = Column(String(10))
    telefono_alumno = Column(String(5))
    email_alumno = Column(String(100))
    descuento_familiar = Column(Float, default=0.0)

