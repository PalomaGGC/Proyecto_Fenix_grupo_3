from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@loclhost:3306/database_fenix")

conexion = engine.connect()

meta = MetaData()