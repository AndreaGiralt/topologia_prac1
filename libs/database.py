from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

class Database ():

    collection = None

    def __init__(self):

        settings = get_project_settings()
        client = MongoClient(host=settings['MONGODB_SERVER'],port= settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def store_item(self,item):

        print("insertaaaaa")

        print (item)
        self.collection.update({'id': item['id']}, dict(item), upsert=True)
        return item

    def getFormatedIDs (self):

        result = self.db.ids.distinct("id")
        # Se puede llamar a la API de 25 en 25.
        chunks = 25

        output = ["|".join(result[i:i + chunks]) for i in range(0, len(result), chunks)]

        return output


    def getRealStates(self):

        result = self.db.details.find({})

        return result