from sqlalchemy import Boolean, ForeignKey, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine

#creo el modelo de la tabla
tabla_inscripciones = Table("inscripciones", meta, 
    Column("id_inscripciones", Integer, primary_key=True,  autoincrement=True),
    Column("alumnos_ID", Integer, ForeignKey("alumnos.id_alumnos")),
    Column("clases_ID", Integer, ForeignKey("clases.id_clases")),
    Column("niveles", Integer)
)

#creo la tabla en la base de datos
meta.create_all(engine)