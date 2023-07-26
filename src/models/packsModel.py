from sqlalchemy import Boolean, ForeignKey, Numeric, Table, Column, String, Float
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base


#MODELO DE LA TABLA
class Packs_model(Base):

    __tablename__ = "packs"
    id_pack = Column(Integer, primary_key=True,  autoincrement=True)
    nombre_pack =Column(String(100))
    precio_pack =Column(Float)
    primer_descuento =Column(Float)
    segundo_descuento =Column(Float)

    
    