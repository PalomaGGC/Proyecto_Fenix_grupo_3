from sqlalchemy import ForeignKey, Column,String
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base

#MODELO DE LA TABLA
class Inscripciones_model(Base):
    __tablename__ = "inscripciones"
    id_inscripciones = Column(Integer, primary_key=True,  autoincrement=True)
    alumnos_id = Column(Integer, ForeignKey("alumnos.id_alumno"))
    profesor_clase_id = Column(Integer)
    precio_clase = Column(Integer)
    descuento_inscripcion = Column(Integer)
    precio_con_descuento = Column(Integer)
    estado_inscripcion = Column(String(10))
    fecha_inscripcion = Column(String(20))

