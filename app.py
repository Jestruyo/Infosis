from flask import Flask, jsonify, request
from Utils.Validations import validate_data
from congregation.congregation import Congregation
from users.users import User

# App initialization.
app = Flask(__name__)

# Class instances.
congregation = Congregation()
users = User()

# Definition of the route.
@app.route("/users_congregation/", methods = ["GET"])
def consult_register():

    """
    Route that shows the list of brothers in the congregation, registered in the users table.
    
    Ruta que muestra la lista de hermanos de la congregacion, registrados en la tabla usuarios.
    """
    try:

        res = congregation.consult_users()
        return jsonify(res)

    except Exception as e:
        return str(e)  # Returns the error as a string.
    

# Definition of the route.
@app.route("/user_register/", methods = ["POST"])
def register():

    """
    Route that makes a new record in the users table.
    
    Ruta que realiza un nuevo registro en la tabla usuarios.
    """
    try:

        # Dictionary of required data.
        data_new_user = {

            "PRIMER_NOMBRE":request.json["PRIMER_NOMBRE"],
            "SEGUNDO_NOMBRE":request.json["SEGUNDO_NOMBRE"],
            "PRIMER_APELLIDO":request.json["PRIMER_APELLIDO"],
            "SEGUNDO_APELLIDO":request.json["SEGUNDO_APELLIDO"],
            "EDAD":request.json["EDAD"],
            "SEXO":request.json["SEXO"],
            "GRUPO":request.json["GRUPO"],
            "PRIVILEGIO_SERVICIO":request.json["PRIVILEGIO_SERVICIO"],
            "TELEFONO_1":request.json["TELEFONO_1"],
            "TELEFONO_2":request.json["TELEFONO_2"],
            "CORREO":request.json["CORREO"],
            "DIRECCION":request.json["DIRECCION"]

        }
        
        # Json data validator.
        validate_data(data_new_user,"register")

        # Registration function.
        register_user = users.user_registration(data_new_user)
        return jsonify(register_user)

    except Exception as e:
        return str(e)  # Returns the error as a string.
    


# Definition of the route.
@app.route("/log_reports/", methods = ["POST"])
def reports():

    """
    Route that performs a new service report record.
    
    Ruta que realiza un nuevo registro de informe de servicio.
    """
    try:

        # Dictionary of required data.
        data_new_report = {

            "ID_USUARIO":request.json["ID_USUARIO"],
            "HORAS":request.json["HORAS"],
            "PUBLICACIONES":request.json["PUBLICACIONES"],
            "REVISITAS":request.json["REVISITAS"],
            "ESTUDIOS":request.json["ESTUDIOS"]

        }
        
        # Json data validator.
        validate_data(data_new_report,"reports")

        # Registration function.
        register_user = users.log_reports(data_new_report)
        return jsonify(register_user)

    except Exception as e:
        return str(e)  # Returns the error as a string.
    


# Definition of the route.
@app.route("/filter_privileges_congregation/", methods = ["POST"])
def filter_privileges():

    """
    Route that shows the list filtered by privileges.

    Rura que muestra el listado filtrado por privilegios.
    """
    try:

        data = {
            "ID_PRIVILEGIO":request.json["ID_PRIVILEGIO"]
        }

        # Json data validator.
        validate_data(data,"filter_privileges")

        # Consult function.
        res = congregation.filter_privileges(data)
        return jsonify(res)

    except Exception as e:
        return str(e)  # Returns the error as a string.

# Initialization of the local server, if __name__ is the main file.
if __name__ == "__main__":
    app.run(debug=True)
