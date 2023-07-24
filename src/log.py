import logging
import mysql.connector
from mysql.connector import Error
#import inspect

class Connect_DB():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host = 'localhost', database ='FENIX2', user = 'root', password = 'root')
            if self.connection.is_connected():
                self.cursor =self.connection.cursor()
        except Error as e:
            print (f'No puedo connectar a database {e}')

    def execute_query(self, sql):
        self.cursor.execute(sql)

    def close_connection(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

class CustomHandler(logging.StreamHandler):

    def __init__(self, db):
        super().__init__()
        self.db = db

    def emit(self, record):
        if record:
            self.db.execute_query(f"INSERT INTO LOGS VALUES('{record.filename}', '{record.funcName}', '{record.lineno}', '{record.msg}', SYSDATE())")
   

def main(logger, db):
    try:
        
        logger.debug('Este es el modo de debug')
        logger.info ('Este es el modo de info')
        logger.warning('Este es el modo de warning')
        logger.error('Este es el modo de error')
        logger.critical('Este es el modo de critical')
        
    finally:
        db.close_connection()

if __name__ == "__main__":
    db = Connect_DB()
    logger = logging.Logger("FENIX2")
    logger.setLevel(logging.DEBUG)
    customhandler = CustomHandler(db)
    logger.addHandler(customhandler)
    main(logger, db)

