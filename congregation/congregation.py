from Utils.Database import Database
from Utils.Response import Response
from models.model_usuarios_table import Model_usuarios as U
import json


class Congregation(Response):

    def consult_users(self) -> dict:

        """
        Method in charge of consulting the registered users
        in the congregation's database.

        Metodo encargado de consultar los usuarios registrados
        en la base de datos de la congregacion.
        """

        # Database instance.
        db = Database("dbr").session
        
        try:

            query = db.query(U).all()
            res = json.loads(str(query))
            return res

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()



    def consult_congregation_privilegios(self, data:dict) -> dict:

        """
        Method in charge of consulting the registered users
        in the users table where service_privilege = 6 or (Elder).

        Metodo encargado de consultar los usuarios registrados
        en la tabla usuarios donde privilegio_servicio = 6 o (Anciano)
        """

        # Database instance.
        db = Database("dbr").session
        
        try:

            id_privilegio = data["ID_PRIVILEGIO"]
            query = db.query(U).filter(U.PRIVILEGIO_SERVICIO == id_privilegio).all()
            res = json.loads(str(query))
            return res

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()