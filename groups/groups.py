from Utils.Database import Database
from Utils.Response import Response
from models.model_groups_table import Model_groups as G

class Groups(Response):

    def update_group_members(self, data:dict) -> bool:

        """
        Method in charge of updating the number of members of a group, according to the ID.

        Metodo encargado de actualizar el numero de integrantes de un grupo, de acuerdo al ID.
        """

        # Database instance.
        db = Database("dbr").session

        try:

            # Consult the corresponding group.
            query = db.query(G).filter(G.ID == data["ID"]).first()

            if query:

                # Members update.
                query.NUMERO_DE_INTEGRANTES +=1
                db.commit()
                return True
            
            else:

                return False

        except Exception as e:
            raise ValueError(e)
        
        # Termination and closure of connection.
        finally:
            db.invalidate()
            db.close()