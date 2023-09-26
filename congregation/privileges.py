from Utils.Database import Database
from Utils.Response import Response
from models.model_privileges_table import Model_privileges as p

class Privileges(Response):


    def log_privileges(self, data:dict) -> dict:

        """
        Method responsible for storing the existing privileges in a congregation.

        Método encargado de almacenar los privilegios existentes en una congregación.
        """

        # Database instance.
        db = Database("dbr").session

        try:

            new_privileges = p(data)
            db.add(new_privileges)
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