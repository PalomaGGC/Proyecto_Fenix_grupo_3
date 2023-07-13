from sqlalchemy import Boolean, Float, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine

#creo el modelo de la tabla
tabla_descuentos = Table("descuentos", meta, 
    Column("id_descuento", Integer, primary_key=True,  autoincrement=True),
    Column("tipo_descuento", String(100)),
    Column("porcentage_descuento", Integer),
)

#creo la tabla en la base de datos
meta.create_all(engine)