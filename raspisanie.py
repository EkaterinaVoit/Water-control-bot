import telebot
import datetime
import time
from datetime import datetime
from telebot import types
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

bot = telebot.TeleBot("1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg")
TOKEN = '1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg'
bot = telebot.TeleBot(TOKEN)
chat_id= '1506364107'
user_id='485308239'



#отправка сообщения в заданное нами время:
import schedule
import time

def job():
    bot.send_message(user_id, "I'm working...")


schedule.every().day.at("16:10").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



