from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Model_privileges(Base):

    __tablename__ = "PRIVILEGIOS"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    TIPO = Column(String(150), nullable=False)

    def __init__(self, payload):

        self.TIPO = payload["TIPO"]

    def __repr__(self) -> str:

        column = {

            'ID':self.ID,
            'TIPO':self.TIPO
        }
        return json.dumps(column, default=str)