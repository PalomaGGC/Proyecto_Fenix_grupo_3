from sqlalchemy import Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine, Base



# Creo el modelo de la tabla Profesores
class Profesores_model(Base):
    __tablename__ = "profesores"
    id_profesor = Column(Integer, primary_key=True,  autoincrement=True)
    nombre_profesor = Column(String(100))
    apellido_profesor = Column(String(100))
    email_profesor = Column(String(50))


