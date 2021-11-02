from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

from items import RealStateItem

class Database ():

    collection = None
    unEmploymentCollection = None

    def __init__(self):

        settings = get_project_settings()
        client = MongoClient(host=settings['MONGODB_SERVER'],port= settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.unEmploymentCollection = db[settings['MONGODB_UNEMPLOYMENT_COLLECTION']]

    def store_item(self,item):
        self.collection.update({'id': item['id']}, dict(item), upsert=True)
        return item

    def getFormatedIDs (self):

        result = self.collection.distinct("id")

        # Se puede llamar a la API de 25 en 25.
        chunks = 25

        output = ["|".join(result[i:i + chunks]) for i in range(0, len(result), chunks)]
        return output

    def getItem (self,id):
        result = self.collection.find({"id":id})
        if result:
            item = RealStateItem(result[0])
            return item

    def getRealStates(self):

        result = self.collection.find({})
        return result

    def storeUnemploymentInfo(self,items):
        self.unEmploymentCollection.drop()
        self.unEmploymentCollection.insert_many(items)
