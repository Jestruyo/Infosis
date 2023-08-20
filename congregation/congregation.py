from Utils.Database import Database
from Utils.Response import Response
from models.model_usuarios_table import Model_usuarios as U
import json


class Congregation(Response):

    def consult_users(self):

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