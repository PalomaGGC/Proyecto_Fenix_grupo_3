from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Column,String, Integer,func
from dateutil.relativedelta import relativedelta
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
    fecha_inscripcion = Column(DateTime)
    fecha_fin = Column(DateTime)
  
    
    # def __init__(self, *args, **kwargs):
    #     super(Inscripciones_model, self).__init__(*args, **kwargs)
    #     # Calcular manualmente la fecha de fin sumando un mes a la fecha de inicio
    #     self.fecha_fin = self.fecha_inscripcion + relativedelta(months=1)


