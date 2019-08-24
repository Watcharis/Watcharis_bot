from databases import data_monly,data_word


def query(text):
    db = data_word()
    result = db.word.find_one({"ask" : text})
    print(result)
   
    if result == None:
        return "default"
    
    body =  result['ans']
    # for item in body:
    #     if item['text'] == text :

    #         print(item['text'])
    return body

# test = query("สวสัดีจ้า")
# print(test)





# class Query:

#     def __init__(self):
#         self.query = query


# query = Query()


# result = query.query("xxx")


# print(result)