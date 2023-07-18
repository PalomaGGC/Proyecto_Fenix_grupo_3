from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import Integer, Float 
from config.db import Base

#MODELO DE LA TABLA
class Descuento_model(Base):
    __tablename__= "descuentos"
    id_descuento = Column( Integer, primary_key=True,  autoincrement=True)
    tipo_descuento = Column(String(100))
    porcentage_descuento = Column( Float)
