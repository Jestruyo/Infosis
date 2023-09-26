from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import NoSuchModuleError
# from Utils.Aws import Aws

class Database:

    def __init__(self, mode : str = "dbr"):
        """
        Constructor Method in charge of making the connection to the database, it's important to bear in mind that to make the connection, it must be made based on a mode:
        
        Modes:
            - dbr -> Mode read
            - dbw -> Mode write

        """
        # secret = Aws.get_secret()

        try:
                                                            
            if mode == 'dbr':
                # Conexion SECRETOS
                # connection_data = {
                #     "username": secret.get("username_bd", ""),
                #     "password": secret.get("password_bd", ""),
                #     "host": secret.get("host_bd", ""),
                #     "bd_name": secret.get("name_bd", "")
                # }

                # Conexion LOCAL
                connection_data = {
                    "username": "root",
                    "password": "123123",
                    "host": "localhost",
                    "bd_name": "infosis"
                }

            elif mode == "dbw":
                # Conexion SECRETOS
                # connection_data = {
                #     "username": secret.get("username_bd", ""),
                #     "password": secret.get("password_bd", ""),
                #     "host": secret.get("host_bd", ""),
                #     "bd_name": secret.get("name_bd", "")
                # }

                # Conexion LOCAL
                connection_data = {
                    "username": "root",
                    "password": "123123",
                    "host": "localhost",
                    "bd_name": "infosis"
                }

            else:
                raise Exception("The database usage mode is invalidad.")
            
            database_url = f"mysql+mysqlconnector://{connection_data['username']}:{connection_data['password']}@{connection_data['host']}/{connection_data['bd_name']}"

            engine = create_engine(database_url, poolclass=QueuePool)

            session_maker = sessionmaker(bind = engine)
    
            self.session = session_maker()

        except NoSuchModuleError:
            raise NoSuchModuleError("Can't load plugin.")
        
        except Exception as e:
            raise Exception(e)

