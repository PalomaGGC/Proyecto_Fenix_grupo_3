
from sqlalchemy import Float, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base


#MODELO DE LA TABLA
class Niveles_model(Base):
    __tablename__ = "niveles"
    id_nivel = Column(Integer, primary_key=True,  autoincrement=True)
    nombre_nivel = Column(String(100))

   


