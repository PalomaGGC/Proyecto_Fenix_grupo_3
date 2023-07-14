from sqlalchemy import Boolean, ForeignKey, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine
from config.db import Base


class Inscripciones(Base):
#creo el modelo de la tabla
    __tablename__ = "inscripciones"
    id_inscripciones = Column(Integer, primary_key=True,  autoincrement=True)
    alumnos_id = Column(Integer, ForeignKey("alumnos.id_alumnos"))
    profesor_clase_id = Column(Integer, ForeignKey(""))
    fecha_inscripcion = Column(str)



#creo la tabla en la base de datos
meta.create_all(engine)