from pymongo import MongoClient

def data_word():
    client = MongoClient("mongodb+srv://Watcharis:1f3cfe8a@botautochat-swywi.mongodb.net/test?retryWrites=true&w=majority")
    db = client["lineword"]
    return db

def data_monly():
    client = MongoClient("localhost",27017)
    db = client["monly"]
    return db

# d = data_word()
# d.test.insert({"test": "test"})
# print(d.test.find_one({"test":"test"}))git 