from flask import jsonify, request
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

from pymongo import MongoClient
from databases import data_word
from data_message import query

import base64
import hashlib
import hmac
import json
import requests
import pymongo
import inspect
import collections
import bson
from bson.codec_options import CodecOptions

class ReplyMessages:

    def __init__(self):

        self.headers = {
            'Content-Type':'application/json',
            'Authorization' :'Bearer LL8EKcdxoDmo4jam3iPXZAx4xNCXV7VXxGEgGQ9bqBggmZO4xDLkOLowAhEaS0dlNck2N1rb765KIedconoPTUpUAo+aakEqt7XvN4T+zwTf7N4LwQu3At4wbSruPU4QRjwPWS12VVoa9dvD+xqmjgdB04t89/1O/w1cDnyilFU='
        }
        self.url = 'https://api.line.me/v2/bot/message/reply'
        self.db = data_word()
        self.query = query
        


    def refect_token(self,text,token):
        # try:
        #     print(self.query)
        #     text_from_db = self.query(text)
        # except Exception as e:
        #     print(e)
        # print(text_from_db)
        
        headers = self.headers
        url = self.url
        mess = {
            "replyToken":  token,
            "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
        }
        
        response = dict()
        response['headers'] = headers
        response['url'] = url
        response['mess'] = mess
        return mess
    
    def send_image(self, img_url, thumb_url, song_name, token):
        headers = self.headers
        url = self.url
        mess = {
            "replyToken":  token,
            "messages":[
                {
                    "type":"text",
                    "text": song_name 
                },
                {
                    "type": "image",
                    "originalContentUrl": "https://example.com/original.jpg",
                    "previewImageUrl": "https://example.com/preview.jpg"
                }
            ]
        }
        response = dict()
        response['headers'] = headers
        response['url'] = url
        response['mess'] = mess
        return mess

    
    def handles_message(self):
        return jsonify(self.refect_token('test_reply_token', 123456789))


    def handle_message(self): 

        header = request.headers.get("x-line-signature")
        print(header)

        try:
            bodys = request.get_data(as_text=True)
            print(bodys)
        except Exception as e:
            return jsonify({"status" : 400},{"message":"invalid body"}),400
        
        try:
            channel_secret = "0147ad3c8e4bd2b673af819225173a01"
        except Exception as e:
            return jsonify({"status" : 403},{"message":"invalid channel_secret"}),403

        try:
            body = json.loads(bodys)
            _body_event = body['events']
            for item in _body_event:
                token = item['replyToken']
                print("token: ", token)
        except Exception as e:
            return jsonify({"status" : 402},{"message":"invalid body"}),402
        
        
        try:
            hash = hmac.new(channel_secret.encode('utf-8'),bodys.encode('utf-8'), hashlib.sha256).digest()
            signature = base64.b64encode(hash)
            print(type(signature))
            signatures = signature.decode("utf-8")
            print(signatures)
        except Exception as e:
            print(e)
            return jsonify({"status" : 404},{"message":"invalid body post methods"}),404

        try:
            if header != signatures :
                print("error")
            else:
                print("successful")
        except :
            return jsonify({"status" : 500},{"message":"server error"}),500
        

        text = _body_event[0]['message']['text']

        print("text: ", text)
        
        try:
            messages = self.refect_token('test', token)
            print(json.dumps(messages))
            req = requests.post(url = self.url , data=json.dumps(messages), headers=self.headers)
        except Exception as e:
            print(e)
            return jsonify({"status": 400})
 
        
        return jsonify({"status":200})
















