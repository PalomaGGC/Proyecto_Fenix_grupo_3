from sqlalchemy import Float, Column, ForeignKey, String, DateTime
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base

class Pagos_model(Base):
    __tablename__ = "pagos"
    id_pago = Column(Integer, primary_key=True,  autoincrement=True)
    inscripcion_id = Column(Integer, ForeignKey("inscripciones.id_inscripcion"))
    fecha_pago = Column(String(20))