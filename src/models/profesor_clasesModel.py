from sqlalchemy import ForeignKey, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine, Base

# Creo el modelo de la tabla Profesores
class Profesor_clases_model(Base):
    __tablename__ = "profesores_clases"
    id_clase_profesor = Column(Integer, primary_key=True, autoincrement=True)
    clase_id = Column(Integer, ForeignKey("clases.id_clase"))
    profesor_id = Column(Integer, ForeignKey ("profesores.id_profesor"))
    nivel_id = Column(Integer, ForeignKey("niveles.id_nivel"))
