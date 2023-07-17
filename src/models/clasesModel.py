from sqlalchemy import Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import Base


#MODELO DE LA TABLA
class Clases_model(Base): 
__tablename__ = "clases"
    id_clases =Column(Integer, primary_key=True,  autoincrement=True),
    nombre_clase =Column(String(50))
    packs_id =Column(Integer, ForeignKey("packs.id_pack"))

)


#creo la tabla en la base de datos
# meta.create_all(engine)