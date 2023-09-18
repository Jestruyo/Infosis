from jsonschema import validate, FormatChecker, ValidationError, SchemaError
import json

def validate_data(instance : dict, name_object : str = "") -> None:
    """
    Method in charge of performing validations considering the JSON format, it always receives a payload through which it is validated with a set of rules parameterized in a schema.
    rules parameterized in a schema.

    Return:
        - Responsible for raising an exception that reaches the handler and depending on the exception returns a response to the request.
    """
    try:
        with open("jsonschema.json", "r") as file:
            schema = json.load(file)
            file.close()

        if len(name_object) != 0:
            schema = schema[name_object]
    
        validate(instance = instance, schema = schema, format_checker = FormatChecker)

    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory.")
    
    except TypeError:
        raise TypeError("Argument is not iterable.")
    
    except AttributeError:
        raise AttributeError("Object has no attribute 'read'.")
    
    except OSError:
        raise OSError("Invalid argument.")
    
    except SchemaError:
        raise SchemaError("The data provided is not of type object.")
    
    except ValidationError as e:

        messages = {
            "required" : "The fields are required.",
            "type" : "Data types do not match.",
            "minLength" : "The fields are too short.",
            "maxLength" : "The fields are too long",
            "pattern" : "The fields does not match.",
            "enum" : "The fields does not match.",
            "multipleOf" : "The fields are not multiples.",
            "minimum" : "The fields are less than the minimum",
            "maximum" : "The fields are greater than the maximum",
            "exclusiveMinimum" : "The fields are less than or equal to the minimum.",
            "exclusiveMaximum" : "The fields are greater than or equal to the maximum.",
            "minItems" : "The fields are too short.",
            "maxItems" : "The fields are too long.",
            "uniqueItems" : "The fields have non-unique elements."
        }    

        if e.validator in messages:
            message = messages[e.validator]
        
        else:
            message = e.message

        raise ValidationError(message)