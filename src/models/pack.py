from sqlalchemy import Boolean, Numeric, Table, Column, String, Float
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine


#creo el modelo de la tabla
tabla_pack = Table("pack", meta, 
    Column("id_pack", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_pack", String(100)),
    Column("precio_pack", String(100)),
)

#creo la tabla en la base de datos
meta.create_all(engine)