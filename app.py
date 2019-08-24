from flask import Flask, jsonify, request
# from linebot import LineBotApi
# from linebot.exceptions import LineBotApiError
# from linebot.models import (
#  MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
#  SourceUser, SourceGroup, SourceRoom,
#  TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
#  ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
#  CarouselTemplate, CarouselColumn, PostbackEvent,
#  StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
#  ImageMessage, VideoMessage, AudioMessage,
#  UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
# )

# from pymongo import MongoClient
# from databases import data_word
# from function import ReplyMessages

# import base64
# import hashlib
# import hmac
# import json
# import requests
# import pymongo
# import inspect
# import collections
# import bson
# from bson.codec_options import CodecOptions




app = Flask(__name__)

# reply_message = ReplyMessages()


@app.route("/api",methods =["GET"])
def api_root():
    return jsonify({"status":200})


# @app.route("/api_lines",methods = ["GET"])
# def api_lines():
#     return reply_message.handles_message()

# @app.route("/api_line",methods = ["POST"])
# def api_line():
#     return reply_message.handle_message()
    

    
    






if __name__ == "__main__":
    
    #app.run(debug=True)
    print (app.url_map)
    
    app.run(host='0.0.0.0', port=5000)
