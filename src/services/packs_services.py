from sqlalchemy.exc import SQLAlchemyError
from models.packsModel import Packs_model
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from config.db import Session


class Packs_services:
    def __init__(self) -> None:
        #db para que cada vez que se ejecute ese servicio
        #se envíe una sesión a la base de datos
        self.db = Session()
        #ya puedo acceder a la base de datos desde otros métodos

    # CONSULTAR TODOS LOS PACKS
    def consultar_packs(self):
        try:
            result = self.db.query(Packs_model).all()
            #obtengo todos los datos Packs_model y los guardo en la variable result
            return result
        except SQLAlchemyError as e:
            # Si ocurre un error en la consulta, se lanza una excepción HTTP con el código de estado 500 y el detalle del error
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # CONSULTAR UN PACK
    def consultar_pack_por_id(self, id):
        try:
            result = self.db.query(Packs_model).filter(Packs_model.id_pack == id).first()
            #obtengo los datos de el pack que quiero consultar filtrando por id, 
            # obtengo los del primero que encuentre y los guardo en la variable result
            if not result:
                # Si no se encuentra el pack, se lanza una excepción HTTP con el código de estado 404 y un mensaje de error
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pack no encontrado")
            return result
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # AGREGAR UN PACK
    def agregar_pack(self, data):
        try:
            pack = self.db.query(Packs_model).filter(Packs_model.id_pack == data.id_pack).first()
            print(data)
            if pack:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ya existe un pack con este id")

            nuevo_pack = Packs_model(**data.dict())
            #Le envío el nuevo pack
            self.db.add(nuevo_pack)
            #Hago el commit para que se actualice
            self.db.commit()
            return f"Se agregó el pack {nuevo_pack} correctamente"
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # EDITAR UN PACK
    def editar_pack(self, id: int, data):
        try:
            pack = self.db.query(Packs_model).filter(Packs_model.id_pack == id).first()
            if not pack:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pack no encontrado")

            pack.nombre_pack = data.nombre_pack
            pack.precio_pack = data.precio_pack
            pack.primer_descuento = data.primer_descuento
            pack.segundo_descuento = data.segundo_descuento

            self.db.commit()
            return {"message": "Pack actualizado correctamente"}
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # BORRAR UN PACK
    def borrar_pack(self, id: int):
        try:
            pack = self.db.query(Packs_model).filter(Packs_model.id_pack == id).first()
            if not pack:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe ningún pack con ese id")
            self.db.query(Packs_model).filter(Packs_model.id_pack == id).delete()
            self.db.commit()
            return
        except SQLAlchemyError as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)