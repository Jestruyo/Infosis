import json

class Response:

    @classmethod
    def response(cls, data : any = {}) -> dict:
        """
        Method in charge of returning a data with the appropriate format to be displayed as a request response.

        """
        return {"statusCode": data["statusCode"], "body": json.dumps(data), "headers": {'Content-Type': 'application/json'}}
    
    #200-299
    @classmethod
    def success(cls, data : any = {}, message : str = "Satisfactory service.") -> dict:
        """
        Method responsible for returning a satisfaction response.

        """
        data = {
            "message" : message,
            "statusCode" : 200,
            "data" : data
        }

        return cls.response(data)

    @classmethod
    def created(cls, data : any = {}, message : str = "Created.") -> dict:
        """
        Method in charge of returning a satisfaction response for creation processes.

        """
        data = {
            "message" : message,
            "statusCode" : 201,
            "data" : data
        }

        return cls.response(data)
    
    @classmethod
    def accepted(cls, message : str = "Accepted.") -> dict:
        """
        Method responsible for returning a response indicating that the request has been received but not yet acted upon.
        
        """
        data = {
            "message" : message,
            "statusCode" : 202
        }

        return cls.response(data)

    @classmethod
    def no_content(cls) -> dict:
        """
        The request has been completed successfully but its response has no content.

        """
        data = {
            "statusCode" : 204
        }

        return cls.response(data)
    
    @classmethod
    def reset_content(cls, message : str = "Reset content.") -> dict:
        """
        The request has been completed successfully, but its response has no contents and in addition, the user agent has to initialize the page from which the request was made.

        """
        data = {
            "message" : message,
            "statusCode" : 205
        }

        return cls.response(data)
    
    #300-399
    @classmethod
    def not_modified(cls) -> dict:
        """
        This is used for caching purposes. It tells the client that the response has not been modified.

        """
        data = {
            "statusCode" : 304
        }

        return cls.response(data)
    
    #400-499
    @classmethod
    def bad_request(cls, message : str = "Bad request.") -> dict:
        """
        This response means that the server could not interpret the request given an invalid syntax.

        """
        data = {
            "message" : str(message),
            "statusCode" : 400
        }

        return cls.response(data)
    
    @classmethod
    def unauthorized(cls, message : str = "Unauthorized.") -> dict:
        """
        Authentication is required to obtain the requested response. This is similar to 403, but in this case, authentication is possible.

        """
        data = {
            "message" : message,
            "statusCode" : 401
        }

        return cls.response(data)
    
    @classmethod
    def forbidden(cls, message : str = "Forbidden.") -> dict:
        """
        The client does not have the necessary permissions for certain content, so the server is refusing to give an appropriate response.

        """
        data = {
            "message" : message,
            "statusCode" : 403
        }

        return cls.response(data)
    
    @classmethod
    def not_found(cls, message : str = "Not found.") -> dict:
        """
        The server could not find the requested content.

        """
        data = {
            "message" : message,
            "statusCode" : 404
        }

        return cls.response(data)
    
    @classmethod
    def gone(cls, message : str = "Gone.") -> dict:
        """
        This response can be sent when the requested content has been deleted from the server.

        """
        data = {
            "message" : message,
            "statusCode" : 410
        }

        return cls.response(data)
    
    @classmethod
    def length_required(cls, message : str = "Length required.") -> dict:
        """
        The server rejects the request because the Content-Length header field is not defined and the server requires it.

        """
        data = {
            "message" : message,
            "statusCode" : 411
        }

        return cls.response(data)

    #500-599
    @classmethod
    def internal_server_error(cls, error : any = Exception) -> dict:
        """
        The server has encountered a situation that it does not know how to handle.

        """
        type_error = (str(type(error))).split("'")

        if type(error) is KeyError:
            error = "The key object provided is missing."
    
        data = {
            "message" : str(error),
            "error" : type_error[1],
            "statusCode" : 500
        }

        return cls.response(data)



