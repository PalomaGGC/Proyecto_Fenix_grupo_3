from sqlalchemy import Boolean, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine


#MODELO DE LA TABLA
tabla_niveles = Table("niveles", meta, 
    Column("id_niveles", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_nivel", String(100)),
)

#creo la tabla en la base de datos
meta.create_all(engine)