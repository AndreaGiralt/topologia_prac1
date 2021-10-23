from pymongo import MongoClient

class Database ():

    client = None
    db = None

    def __init__(self):
        #TODO Crear la bd y la colección si no existe.
        self.client = MongoClient(host="mongo_uoc")
        self.db = self.client.real_states

    def insertID(self,id):
        result = self.db.ids.insert_one({"id":id})
