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






