import base64
import hashlib
import hmac



    channel_secret = "0147ad3c8e4bd2b673af819225173a01"
    body = json.dump(body)
    hash = hmac.new(channel_secret.encode('utf-8'),body.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(hash)