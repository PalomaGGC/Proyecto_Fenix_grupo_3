from sqlalchemy import create_engine, MetaData

#aqui hago la conexion a la base de datos... la base de datos se llama (database_fenix)
engine = create_engine("mysql+pymysql://root:@localhost:3306/database_fenix")
#guardo la conexion en una variable para despues utilizarla en otros archivos
conexion = engine.connect()
# MetaData actúa como un contenedor para mantener información sobre las tablas, columnas,
# relaciones y otros elementos de la base de datos. Se utiliza para definir y manipular estructuras de la base de datos en SQLAlchemy.
meta = MetaData()