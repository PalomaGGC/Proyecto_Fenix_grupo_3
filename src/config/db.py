from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
from decouple import config

try:
    user= config("USER")
    host= config("HOST")
    db= config("DB")
    url = f"mysql+pymysql://{user}:@{host}:3306/{db}"
    
    # Aquí hago la conexión a la base de datos... la base de datos se llama "database_fenix"
    engine = create_engine(url)
    print(user)
    # Guardo la conexión en una variable para luego utilizarla en otros archivos
    conexion = engine.connect()
    # MetaData actúa como un contenedor para mantener información sobre las tablas, columnas,
    # relaciones y otros elementos de la base de datos. Se utiliza para definir y manipular estructuras de la base de datos en SQLAlchemy.
    meta = MetaData()
except SQLAlchemyError as e:
    print(f"Error al conectar a la base de datos: {e}")
    # Puedes agregar aquí el manejo de la excepción según tus necesidades