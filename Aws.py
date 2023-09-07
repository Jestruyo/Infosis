import boto3, os, base64, json
from botocore.exceptions import ClientError, ParamValidationError

class Aws:
    
    @classmethod
    def get_secret(cls, secret_name : str = "secret-convenios") -> dict:
        try:
            client = boto3.client(service_name='secretsmanager', region_name = os.getenv("REGION"))
            
            response = client.get_secret_value(SecretId= f"{os.getenv('STAGE')}/{secret_name}")

            if 'SecretString' in response:
                secret = response['SecretString']
            else:
                secret = base64.b64decode(response['SecretBinary'])

            return json.loads(secret)

        except ParamValidationError as e:
            raise Exception("Missing required parameter in input.")
        
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                raise Exception("Secrets Manager can't decrypt the protected secret text using the provided KMS key.")
   
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                raise Exception("An error ocurred on the server side.")
 
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                raise Exception("You provided an invalid value for a parameter.")

            elif e.response['Error']['Code'] == 'InvalidRequestException':
                raise Exception("You provided a parameter value that is not valid for the current state of the resource.")
            
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise Exception("We can't find the resource that you asked for.")
        
        except Exception:
            raise Exception("An unexpected error ocurred.")
        