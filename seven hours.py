import telebot
import datetime
import time
import schedule
from datetime import datetime
from telebot import types
import sys

bot = telebot.TeleBot("1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg")

args = sys.argv
user_id_str = args[1]
user_id = int(user_id_str)
print(f"I neeed to send a message to user {user_id}")

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
knopka3 = types.KeyboardButton('Да👍')
knopka4 = types.KeyboardButton('Нет👎')
markup.add(knopka3, knopka4)

def job():
    bot.send_message(user_id, "Вы уже пили воду сегодня?", reply_markup=markup)
schedule.every().day.at("19:00").do(job)

def good_mo():
    bot.send_message(user_id, "Доброе утро! 🌞 \nПопейте,ожалуйста, воду!")
schedule.every().day.at("09:00").do(good_mo)

def good_day():
    bot.send_message(user_id, "Время обеда, а, значит, пора пить воду! 🕑 ")
schedule.every().day.at("15:00").do(good_day)

def good_ev():
    bot.send_message(user_id, "Вечером тоже нужно пить воду! 💗 ")
schedule.every().day.at("21:00").do(good_ev)

def good_ni():
    bot.send_message(user_id, "Доброй ночи! 🌙 \nПопейте, перед сном, пожалуйста! ")
schedule.every().day.at("23:00").do(good_ni)

while True:
    schedule.run_pending()
    time.sleep(1)
