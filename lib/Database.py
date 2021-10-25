from pymongo import MongoClient

class Database ():

    client = None
    db = None

    def __init__(self):
        #TODO Crear la bd y la colección id y details, si no existe.
        self.client = MongoClient(host="mongo_uoc")
        self.db = self.client.real_states

    def insertID(self,id):
        result = self.db.ids.insert_one({"id":id})
        return result

    def getFormatedIDs (self):

        result = self.db.ids.distinct("id")
        # Se puede llamar a la API de 25 en 25.
        chunks = 25

        output = ["|".join(result[i:i + chunks]) for i in range(0, len(result), chunks)]

        return output

    def insertDocuments (self, documents):

        result = self.db.details.insert(documents)

        return result
