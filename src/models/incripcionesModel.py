from sqlalchemy import Boolean, Date, Float, ForeignKey, Column,String, Integer,func
from config.db import Base

#MODELO DE LA TABLA
class Inscripciones_model(Base):
    __tablename__ = "inscripciones"
    id_inscripcion = Column(Integer, primary_key=True, autoincrement=True)
    profesor_clase_id = Column(Integer, ForeignKey("profesores_clases.id_clase_profesor"))
    alumno_id = Column(Integer, ForeignKey("alumnos.id_alumno"))
    precio_clase = Column(String(20))
    descuento_inscripcion = Column(Float)
    descuento_familiar = Column(Float)
    precio_con_descuento = Column(String(10))
    pagada = Column(String(10))
    fecha_inscripcion = Column(Date)
    fecha_fin = Column(Date)
  



