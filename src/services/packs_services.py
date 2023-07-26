from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.packsModel import Packs_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session
from logger import Logs

class Packs_services:
    def __init__(self) -> None:
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = Session()
        #ya puedo acceder a la base de datos desde otros métodos
        self.logger= Logs()

    # CONSULTAR TODOS LOS PACKS
    def consultar_packs(self):
        result = self.db.query(Packs_model).all()
        self.logger.debug('Consultando todos los packs')
        #obtengo todos los datos Packs_model y los guardo en la variable result
        if not result:
            self.logger.warning('No se encontraron packs')
        # Si no se encuentran packs, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aún no hay packs") 
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # CONSULTAR UN PACK POR ID
    def consultar_pack_por_id(self, id):
        result = self.db.query(Packs_model).filter(Packs_model.id_pack == id).first()
        self.logger.debug(f'Consultando pack por id')
        #obtengo los datos de el pack que quiero consultar filtrando por id,
        # obtengo los del primero que encuentre y los guardo en la variable result
        if not result:
            self.logger.warning('No se encontró el pack')
            # Si no se encuentra el pack, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún pack con ese id")
        return JSONResponse(status_code=200, content=jsonable_encoder(result))


    # AGREGAR UN NUEVO PACK
    def agregar_pack(self, data):
        pack = self.db.query(Packs_model).filter(Packs_model.id_pack == data.id_pack).first()
        if pack:
            self.logger.warning('El pack ya existe con este id')
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ya existe un pack con este id")

        nuevo_pack = Packs_model(**data.dict())
        #Le envío el nuevo pack
        self.db.add(nuevo_pack)
        #Hago el commit para que se actualice
        self.db.commit()
        self.logger.info("Se ha registrado un nuevo pack")
        return JSONResponse(status_code=201, content={"message": "Se ha registrado un nuevo pack"})


    # EDITAR UN PACK
    def editar_pack(self, id: int, data):
        pack = self.db.query(Packs_model).filter(Packs_model.id_pack == id).first()
        if not pack:
            self.logger.warning('No se encontró el pack para editar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún pack con ese id")

        pack.nombre_pack = data.nombre_pack
        pack.precio_pack = data.precio_pack
        pack.primer_descuento = data.primer_descuento
        pack.segundo_descuento = data.segundo_descuento

        self.db.commit()
        self.logger.info('Se ha modificado el pack')
        return JSONResponse(status_code=200, content={"message": "Se ha modificado el pack"})


    # BORRAR UN PACK
    def borrar_pack(self, id: int):
        pack = self.db.query(Packs_model).filter(Packs_model.id_pack == id).first()
        if not pack:
            self.logger.warning('No se encontró el pack para borrar')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún pack con ese id")
        self.db.query(Packs_model).filter(Packs_model.id_pack == id).delete()
        self.db.commit()
        self.logger.info('Se ha eliminado el pack')
        return JSONResponse(status_code=200, content={"message": "Se ha eliminado el pack"})
