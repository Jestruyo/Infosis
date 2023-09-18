from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Model_groups(Base):

    __tablename__ = 'GRUPOS'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    SUPER_GRUPO = Column(Integer, nullable=False)
    SIERVO_GRUPO = Column(Integer, nullable=False)
    NUMERO_DE_INTEGRANTES = Column(Integer, default=None)

    def __init__(self, payload):

        self.SUPER_GRUPO = payload["SUPER_GRUPO"]
        self.SIERVO_GRUPO = payload["SIERVO_GRUPO"]
        self.NUMERO_DE_INTEGRANTES = payload["NUMERO_DE_INTEGRANTES"]

    
    def __repr__(self) -> str:

        column = {

            'ID':self.ID,
            'SUPER_GRUPO':self.SUPER_GRUPO,
            'SIERVO_GRUPO':self.SIERVO_GRUPO,
            'NUMERO_DE_INTEGRANTES':self.NUMERO_DE_INTEGRANTES
        }
        return json.dumps(column, default=str)