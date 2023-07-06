from sqlalchemy import Boolean, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine


#creo el modelo de la tabla
tabla_clases = Table("clases", meta, 
    Column("id_clases", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_clase", String(100)),
)

#creo la tabla en la base de datos
meta.create_all(engine)