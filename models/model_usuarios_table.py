from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Model_usuarios(Base):

    __tablename__ = 'USUARIOS'
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    PRIMER_NOMBRE = Column(String(50), nullable=False)
    SEGUNDO_NOMBRE = Column(String(50))
    PRIMER_APELLIDO = Column(String(70), nullable=False)
    SEGUNDO_APELLIDO = Column(String(70))
    EDAD = Column(Integer, nullable=False)
    SEXO = Column(String(10), nullable=False)
    GRUPO = Column(Integer)
    PRIVILEGIO_SERVICIO = Column(Integer)
    TELEFONO_1 = Column(String(100))
    TELEFONO_2 = Column(String(100))
    CORREO = Column(String(100))
    DIRECCION = Column(String(200), nullable=False)

    def __ini__(self, payload):

        self.PRIMER_NOMBRE = payload["PRIMER_NOMBRE"]
        self.SEGUNDO_NOMBRE = payload["SEGUNDO_NOMBRE"]
        self.PRIMER_APELLIDO = payload["PRIMER_APELLIDO"]
        self.SEGUNDO_APELLIDO = payload["SEGUNDO_APELLIDO"]
        self.EDAD = payload["EDAD"]
        self.SEXO = payload["SEXO"]
        self.GRUPO = payload["GRUPO"]
        self.PRIVILEGIO_SERVICIO = payload["PRIVILEGIO_SERVICIO"]
        self.TELEFONO_1 = payload["TELEFONO_1"]
        self.TELEFONO_2 = payload["TELEFONO_2"]
        self.CORREO = payload["CORREO"]
        self.DIRECCION = payload["DIRECCION"]

    def __repr__(self) -> str:

        column = {

            'ID':self.ID,
            'PRIMER_NOMBRE':self.PRIMER_NOMBRE,
            'SEGUNDO_NOMBRE':self.SEGUNDO_NOMBRE,
            'PRIMER_APELLIDO':self.PRIMER_APELLIDO,
            'SEGUNDO_APELLIDO':self.SEGUNDO_APELLIDO,
            'EDAD':self.EDAD,
            'SEXO':self.SEXO,
            'GRUPO':self.GRUPO,
            'PRIVILEGIO_SERVICIO':self.PRIVILEGIO_SERVICIO,
            'TELEFONO_1':self.TELEFONO_1,
            'TELEFONO_2':self.TELEFONO_2,
            'CORREO':self.CORREO,
            'DIRECCION':self.DIRECCION
        }
        return json.dumps(column, default=str)
    
