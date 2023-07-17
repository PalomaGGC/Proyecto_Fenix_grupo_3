from sqlalchemy import DateTime, ForeignKey, Column,String, Integer,func
from config.db import Base

#MODELO DE LA TABLA
class Inscripciones_model(Base):
    __tablename__ = "inscripciones"
    id_inscripciones = Column(Integer, primary_key=True,  autoincrement=True)
    alumno_id = Column(Integer, ForeignKey("alumnos.id_alumno"))
    profesor_clase_id = Column(Integer, ForeignKey("profesores.id_clase_profesor"))
    precio_clase = Column(Integer)
    descuento_inscripcion = Column(Integer)
    precio_con_descuento = Column(Integer)
    estado_inscripcion = Column(String(10))
    pack_id = Column(Integer)
    fecha_inscripcion = Column(DateTime, default=func.now())

