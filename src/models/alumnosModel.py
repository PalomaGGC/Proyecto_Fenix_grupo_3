from sqlalchemy import Boolean, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta

tabla_alumnos = Table("alumnos", meta, 
    Column("id_alumnos", Integer, primary_key=True,  autoincrement=True),
    Column("nombre_alumno", String(100)),
    Column("apellido_alumno", String(100)),
    Column("edad_alumno", String(5)),
    Column("telefono_alumno", String(5)),
    Column("email_alumno", String(100)),
    Column("descuento_familiar", Numeric(precision=10, scale=2), default=0.0)
)