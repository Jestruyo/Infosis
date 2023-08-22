from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import json

Base = declarative_base()

class Model_reports(Base):

    __tablename__ = 'INFORMES'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ID_USUARIO = Column(Integer, nullable=False)
    ID_GRUPO = Column(Integer, nullable=False)
    PRIMER_NOMBRE = Column(String(50), nullable=False)
    SEGUNDO_NOMBRE = Column(String(50))
    PRIMER_APELLIDO = Column(String(70), nullable=False)
    SEGUNDO_APELLIDO = Column(String(70))
    HORAS = Column(Integer,default=0)
    PUBLICACIONES = Column(Integer,default=0)
    REVISITAS = Column(Integer,default=0)
    ESTUDIOS = Column(Integer,default=0)
    FECHA_INFO = Column(DateTime, default=datetime.utcnow)


    def __init__(self,payload):

        self.ID_USUARIO = payload["ID_USUARIO"]
        self.ID_GRUPO = payload["ID_GRUPO"]
        self.PRIMER_NOMBRE = payload["PRIMER_NOMBRE"]
        self.SEGUNDO_NOMBRE = payload["SEGUNDO_NOMBRE"]
        self.PRIMER_APELLIDO = payload["PRIMER_APELLIDO"]
        self.SEGUNDO_APELLIDO = payload["SEGUNDO_APELLIDO"]
        self.HORAS = payload["HORAS"]
        self.PUBLICACIONES = payload["PUBLICACIONES"]
        self.REVISITAS = payload["REVISITAS"]
        self.ESTUDIOS = payload["ESTUDIOS"]

    
    def __repr__(self) -> str:

        column = {

            'ID':self.ID,
            'ID_USUARIO':self.ID_USUARIO,
            'ID_GRUPO':self.ID_GRUPO,
            'PRIMER_NOMBRE':self.PRIMER_NOMBRE,
            'SEGUNDO_NOMBRE':self.SEGUNDO_NOMBRE,
            'PRIMER_APELLIDO':self.PRIMER_APELLIDO,
            'SEGUNDO_APELLIDO':self.SEGUNDO_APELLIDO,
            'HORAS':self.HORAS,
            'PUBLICACIONES':self.PUBLICACIONES,
            'REVISITAS':self.REVISITAS,
            'ESTUDIOS':self.ESTUDIOS,
            'FECHA_INFO':self.FECHA_INFO
        }

        return json.dumps(column, default=str)