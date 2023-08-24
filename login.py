from Utils.Database import Database
from Utils.Response import Response
import jwt
import datetime
from os import getenv
from models.model_usuarios_table import Model_users as U
from models.model_salts_table import Model_salts as S


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
                token = jwt.encode({"username":data["USERNAME"], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, key=getenv("SECRET"), algorithm="HS256")
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



    def log_salt(self, data:dict)-> bool:

        """
        Method in charge of storing the salt that is generated at the moment of the registry.

        Metodo encargado de almacenar la sal que se genera al instante del registro.
        """

        db = Database("dbr").session

        try:
            
            # An instance of the model salt is created and data is passed to it.
            record = S(data)
            db.add(record)
            db.commit()

            # Registration Verification.
            if db.query(S).filter(S.ID_USUARIO == data["ID_USUARIO"], S.SALT == data["SALT"]).first():
                return True
            else:
                return False

        except Exception as e:
            raise ValueError(e)
        
        finally:
            db.invalidate()
            db.close()