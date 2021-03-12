from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

from config import *



 
# Channel Access Token
line_bot_api = LineBotApi(line_access_token)
# Channel Secret
handler = WebhookHandler(line_access_secret)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=(ImageMessage,TextMessage))
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)
    
    
    
    if event.message.text="上傳相片":
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text="請傳送一張照片給我~")])
        if(event.message,ImageMessage):
               line_bot_api.reply_message(event.reply_token,ImageSendMessage(event.message))
               line_bot_api.reply_message(event.reply_token,TextSendMessage(text="傳送成功"))     



        return 0
    
    
        







import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
