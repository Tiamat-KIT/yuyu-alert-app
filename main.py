import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import schedule

bot_api = LineBotApi("Xr5peOrLCaZmtaZQPS+Z+cDI+pnAJp5JC0xxrQImNDTLofjbJbiHB6v2LEOWvj0aG+wYYKQ2ZLkpnuIG0/lCHN+/eSD6fE7rivw9igSH2jPHI1j7B0te0ooRBWorRXHiDBGJcPnkgx3WUyH6xKcYbgdB04t89/1O/w1cDnyilFU=") #インスタンス化
user_id = "U57fac5935318082a3c8737c34644b2bc" #IDを取得]
token = "Xr5peOrLCaZmtaZQPS+Z+cDI+pnAJp5JC0xxrQImNDTLofjbJbiHB6v2LEOWvj0aG+wYYKQ2ZLkpnuIG0/lCHN+/eSD6fE7rivw9igSH2jPHI1j7B0te0ooRBWorRXHiDBGJcPnkgx3WUyH6xKcYbgdB04t89/1O/w1cDnyilFU="
messages = TextSendMessage(text='起動しました') #LINEに送付するメッセージ
bot_api.push_message(user_id, messages=messages)

def main(): 
    messages = TextSendMessage(text='ちゃんとピル飲むんだよ。') #LINEに送付するメッセージ
    bot_api.push_message(user_id, messages=messages)

schedule.every().days.at("21:00").do(main)
    
while True:
    schedule.run_pending()
    sleep(1000)
  