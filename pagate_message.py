from pymongo import MongoClient
from databases import data_word

def data_text():
    db = data_word()
    data = {
        "ask" : "สวัสดีจ้า",
        "ans" : "สวสัดีครับ"
    }

    db.word.insert_one(data)

#d = data_text()
#print(d)

