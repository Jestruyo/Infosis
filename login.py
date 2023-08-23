from Utils.Database import Database
from Utils.Response import Response
import jwt
import datetime
from os import getenv
from models.model_usuarios_table import Model_users as U


class Login(Response):

    def credential_checker(self, data:dict) -> bool:

        """
        Method in charge of validating if the user is already registered.

        Método encargado de validar si el usuario ya se encuentra registrado.
        """

        db = Database("dbr").session

        try:

            query = db.query(U).filter(U.USERNAME == data["USERNAME"], U.PASSWS == data["PASSWS"]).first()
            return query
            
        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()



    def get_tokens(self, data:dict) -> dict:

        """
        Method responsible for generating a user token.

        Metodo encargado de generar un token de usuario.
        """

        db = Database("dbr").session

        try:

            # It is validated that the username and password are registered.
            user = self.credential_checker(data)

            if user:

                # Token generation.
                token = jwt.encode({"username":data["USERNAME"], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, key=getenv("SECRET"), algorithm="HS256")
                return token
            
            else:
                
                # Answer.
                res = {"message":"Authentication Error", "state":401}
                return res

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()