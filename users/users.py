import bcrypt
from Utils.Database import Database
from Utils.Response import Response
from models.model_usuarios_table import Model_users as U
from models.model_reports_table import Model_reports as R
from groups.groups import Groups
from login import Login


class User(Response):

    def user_registration(self, data:dict) -> dict:

        """
        Method in charge of making a record in the users table.

        Metodo encargado de hacer un registro en la tabla usuarios.
        """

        # Database instance.
        db = Database("dbr").session
        login = Login()
        groups = Groups()
        
        try:

            # Random salt generation
            salt = bcrypt.gensalt()

            # The hashed password is generated.
            hashed_password = bcrypt.hashpw(data["PASSWS"].encode("utf-8"),salt)

            # The data dictionary is updated.
            data["PASSWS"] = hashed_password

            # The users model is instantiated and the data is passed to it.
            new_user = U(**data)
            db.add(new_user)
            db.commit()

            # Query for the required data from the salt record.
            query = db.query(U).filter(U.PASSWS == data["PASSWS"]).first()

            # Salt registration data.
            data_log_salt = {"ID_USUARIO":query.ID,"SALT":salt}
            log_salt = login.log_salt(data_log_salt)
            
            # Group update data.
            data_update_group = {"ID":query.GRUPO}
            update_group = groups.update_group_members(data_update_group)

            if log_salt == True and update_group == True:

                # Answer.
                res = {"message":"registration success","state":200}
                return res
            # Warning.
            res = {"message":"Failed to protect user salt, or members update failed","state":400}
            return res

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()



    def log_reports(self, data:dict) -> dict:

        """
        Method in charge of registering a user's report.

        Metodo encargado de registrar el informe de un usario.
        """

        # Database instance.
        db = Database("dbr").session
        
        try:
            
            # Query that brings the complementary data of the person who enters the report.
            query = db.query(U).filter(U.ID == data["ID_USUARIO"]).first()

            # Dates to incorporate the required.
            supplementary_data = {"ID_GRUPO":query.GRUPO,"PRIMER_NOMBRE":query.PRIMER_NOMBRE,"SEGUNDO_NOMBRE":query.SEGUNDO_NOMBRE,
                                  "PRIMER_APELLIDO":query.PRIMER_APELLIDO,"SEGUNDO_APELLIDO":query.SEGUNDO_APELLIDO}
            
            # Data update required.
            data.update(supplementary_data)

            # The reports model is instantiated and the data is passed to it.
            new_report = R(data)
            db.add(new_report)
            db.commit()

            # Answer.
            res = {"message":"Report registered successfully","state":200}
            return res

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()