from sqlalchemy import Float, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base

#MODELO DE LA TABLA
class Alumnos_model(Base):
    __tablename__ = "alumnos"
    id_alumno = Column(Integer, primary_key=True,  autoincrement=True)
    nombre_alumno = Column(String(100))
    apellido_alumno = Column(String(100))
    edad_alumno = Column(String(3))
    telefono_alumno = Column(String(10))
    email_alumno = Column(String(30))
    descuento_familiar = Column(Float, default=0.0)

