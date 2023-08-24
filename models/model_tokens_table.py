from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Model_tokens(Base):

    __tablename__ = 'TOKENS'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_USUARIO = Column(Integer, nullable=False)
    TOKEN = Column(String(300))


    def __init__(self, payload):

        self.ID_USUARIO = payload["ID_USUARIO"]
        self.TOKEN = payload["TOKEN"]

    
    def __repr__(self) -> str:

        column = {

            'ID':self.ID,
            'ID_USUARIO':self.ID_USUARIO,
            'TOKEN':self.TOKEN
        }
        return json.dumps(column, default=str)