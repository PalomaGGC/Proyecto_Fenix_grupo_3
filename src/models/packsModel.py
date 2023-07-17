from sqlalchemy import Boolean, Numeric, Table, Column, String, Float
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base


#MODELO DE LA TABLA
class Packs_model(Base): 

    __tablename__ = "packs"
    id_pack = Column(Integer, primary_key=True,  autoincrement=True),
    nombre_pack =Column(String(100))
    precio_pack =Column(Float)
    primer_descuento =Column(Float)
    segundo_descuento =Column(Float)
)

#creo la tabla en la base de datos
# meta.create_all(engine)