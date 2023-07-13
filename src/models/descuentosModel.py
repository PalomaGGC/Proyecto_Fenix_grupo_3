from sqlalchemy import Boolean, Float, Numeric, Table, Column, String
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine
from config.db import Base

#creo el modelo de la tabla
tabla_descuentos = Table("descuentos", meta, 
    id_descuento = Column( Integer, primary_key=True,  autoincrement=True),
    tipo_descuento = Column( String(100)),
    porcentage_descuento = Column( Integer)
)

#creo la tabla en la base de datos
meta.create_all(engine)