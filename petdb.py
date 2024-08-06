import pymongo 

mongoURI = "mongodb+srv://anjumustad:8888578595%40Python@anjumustad.otnd41c.mongodb.net/"
client = pymongo.MongoClient(mongoURI)

db = client['Pet']
collection = db["pet"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return response.inserted_id

