import telebot
import datetime
import time
import schedule
from datetime import datetime
from telebot import types

bot = telebot.TeleBot("1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg")
TOKEN = '1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg'
bot = telebot.TeleBot(TOKEN)
chat_id= '1506364107'
user_id='485308239'

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
knopka3 = types.KeyboardButton('водичка наполняет меня!')
knopka4 = types.KeyboardButton('прием воды пропущен :(')
markup.add(knopka3, knopka4)

def job():
    bot.send_message(user_id, "Вы уже пили воду сегодня?", reply_markup=markup)

schedule.every().day.at("20:09").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



