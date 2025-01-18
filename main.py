
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['school']
collection = db['students']

data = {'name': 'alice', 'age': 18}


collection.insert_one(data)

print("Inserted documents:")
for document in collection.find():
    print(document)
