from pymongo import MongoClient

def data_word():
    client = MongoClient("localhost",27017)
    db = client["lineword"]
    return db

def data_monly():
    client = MongoClient("localhost",27017)
    db = client["monly"]
    return db

    