from flask import Flask, jsonify, request
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
 SourceUser, SourceGroup, SourceRoom,
 TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
 ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
 CarouselTemplate, CarouselColumn, PostbackEvent,
 StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
 ImageMessage, VideoMessage, AudioMessage,
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

import base64
import hashlib
import hmac
import json




app = Flask(__name__)

# line_bot_api = LineBotApi('LL8EKcdxoDmo4jam3iPXZAx4xNCXV7VXxGEgGQ9bqBggmZO4xDLkOLowAhEaS0dlNck2N1rb765KIedconoPTUpUAo+aakEqt7XvN4T+zwTf7N4LwQu3At4wbSruPU4QRjwPWS12VVoa9dvD+xqmjgdB04t89/1O/w1cDnyilFU=')




@app.route("/api")
def api_root():
    return jsonify({"status":200})


@app.route("/api_line",methods = ["POST"])
def api_roots():
    header = request.headers.get("x-line-signature")
    print(header)

    try:
        bodys = request.get_data(as_text=True)
        # print(bodys)

    except Exception as e:
       
        return jsonify({"status" : 400},{"message":"invalid body"}),400

   

    try:
        channel_secret = "0147ad3c8e4bd2b673af819225173a01"
    except Exception as e:
       
        return jsonify({"status" : 403},{"message":"invalid channel_secret"}),403

    try:
        body = json.loads(bodys)
        _body = body['events']
        
        for item in _body:
            token = item['replyToken']
            print(token)
    
    except:
        return jsonify({"status" : 402},{"message":"invalid body"}),402
    

        
    
    try:
        hash = hmac.new(channel_secret.encode('utf-8'),bodys.encode('utf-8'), hashlib.sha256).digest()
        
        signature = base64.b64encode(hash)
        
        # print(type(signature))
        signatures = signature.decode("utf-8")
        
        print(signatures)
    except Exception as e:
    
        return jsonify({"status" : 404},{"message":"invalid body post methods"}),404

    try:
        if header != signatures :
            print("error")
        else:
            print("successful")
    except :
        
        return jsonify({"status" : 500},{"message":"server error"}),500
    
    # try:
    #     line_bot_api.reply_message('LL8EKcdxoDmo4jam3iPXZAx4xNCXV7VXxGEgGQ9bqBggmZO4xDLkOLowAhEaS0dlNck2N1rb765KIedconoPTUpUAo+aakEqt7XvN4T+zwTf7N4LwQu3At4wbSruPU4QRjwPWS12VVoa9dvD+xqmjgdB04t89/1O/w1cDnyilFU=', TextSendMessage(text='สวัสดีจ้า!'))

    # except LineBotApiError as e:
        
    #     return jsonify({"status":500})

    try:
        
        headers = {
            'Content-Type':'application/json',
            'Authorization' :'Bearer LL8EKcdxoDmo4jam3iPXZAx4xNCXV7VXxGEgGQ9bqBggmZO4xDLkOLowAhEaS0dlNck2N1rb765KIedconoPTUpUAo+aakEqt7XvN4T+zwTf7N4LwQu3At4wbSruPU4QRjwPWS12VVoa9dvD+xqmjgdB04t89/1O/w1cDnyilFU='
            }
        
        url = 'https://api.line.me/v2/bot/message/reply'
        
        mess = {
                'replyToken': token ,
                'messages':[
                    {
                        'type':'text',
                        'text':'เดี่ยวผมติดต่อกลับครับ'
                    },
                    {
                        'type':'text',
                        'text':'ฝากเบอร์ติดต่อไว้ได้เลยครับ'
                    }
                ]
            }
        print(mess)
        print(headers)
        req = requests.post(url , data=json.dumps(mess), headers=headers)
        print(req.headers)        
        
    except:
        return jsonify({"status": 400})
    
    

            
    return jsonify({"status":200})







if __name__ == "__main__":
    
    #app.run(debug=True)
    
    app.run(host='0.0.0.0', port=5000)
