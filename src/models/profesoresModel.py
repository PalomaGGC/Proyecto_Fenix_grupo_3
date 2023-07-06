from sqlalchemy import Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta

tabla_profesores = Table("profesores", meta, 
    Column("id_clases", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_profesor", String(100))
)