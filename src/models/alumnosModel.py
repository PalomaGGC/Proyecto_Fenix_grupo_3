from sqlalchemy import Boolean, Float, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine


#creo el modelo de la tabla
tabla_alumnos = Table("alumnos", meta, 
    Column("id_alumnos", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_alumno", String(100)),
    Column("apellido_alumno", String(100)),
    Column("edad_alumno", String(5)),
    Column("nie_alumno", Integer ),
    Column("telefono_alumno", String(5)),
    Column("email_alumno", String(100)),
    Column("descuento_familiar", Float, default=0.0)
)

#creo la tabla en la base de datos
meta.create_all(engine)