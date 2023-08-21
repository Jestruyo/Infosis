from Utils.Database import Database
from Utils.Response import Response
from models.model_usuarios_table import Model_usuarios as U


class User(Response):

    def user_registration(self, data:dict) -> dict:

        """
        Method in charge of making a record in the users table.

        Metodo encargado de hacer un registro en la tabla usuarios.
        """

        # Database instance.
        db = Database("dbr").session
        
        try:

            # The users model is instantiated and the data is passed to it.
            new_user = U(**data)
            db.add(new_user)
            db.commit()

            # Answer.
            res = {"message":"registration success","state":200}
            return res

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()