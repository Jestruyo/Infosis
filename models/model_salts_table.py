from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import json

Base = declarative_base()

class Model_salts(Base):

    __tablename__ = "SALTS"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_USUARIO = Column(Integer, nullable=False)
    SALT = Column(String(200), nullable=False)
    FECHA_REG = Column(Date, default=datetime.utcnow)


    def __init__(self, payload):

        self.ID_USUARIO = payload["ID_USUARIO"]
        self.SALT = payload["SALT"]


    def __repr__(self) -> str:

        column = {

            'ID':self.ID,
            'ID_USUARIO':self.ID_USUARIO,
            'SALT':self.SALT,
            'FECHA_REG':self.FECHA_REG
        }
        return json.dumps(column, default=str)