from sqlalchemy import Boolean, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta

tabla_clases = Table("clases", meta, 
    Column("id_clases", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_clase", String(100)),
)