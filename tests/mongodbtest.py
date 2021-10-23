from pymongo import MongoClient


client = MongoClient(host="mongo_uoc")
db=client.real_state_ids
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)