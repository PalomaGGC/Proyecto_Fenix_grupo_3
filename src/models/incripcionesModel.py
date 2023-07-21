from sqlalchemy import DateTime, Float, ForeignKey, Column,String, Integer,func
from config.db import Base

#MODELO DE LA TABLA
class Inscripciones_model(Base):
    __tablename__ = "inscripciones"
    id_inscripciones = Column(Integer, primary_key=True, autoincrement=True)
    profesor_clase_id = Column(Integer)
    alumno_id = Column(Integer, ForeignKey("alumnos.id_alumno"))
    # profesor_clase_id = Column(Integer, ForeignKey("profesores_clases.id_clase_profesor"))
    precio_clase = Column(String)
    descuento_inscripcion = Column(Float)
    precio_con_descuento = Column(String)
    estado_inscripcion = Column(String(10))
    fecha_inscripcion = Column(DateTime, default=func.now())


