import telebot
import datetime
import time
import schedule
from datetime import datetime
from telebot import types

bot = telebot.TeleBot("1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg")
TOKEN = '1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg'
bot = telebot.TeleBot(TOKEN)

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
knopka3 = types.KeyboardButton('Да👍')
knopka4 = types.KeyboardButton('Нет👎')
markup.add(knopka3, knopka4)

def job():
    bot.send_message(message.from_user.id, "Вы уже пили воду сегодня?", reply_markup=markup)

schedule.every().day.at("18:00").do(job)

def good_mo():
    bot.send_message(message.from_user.id, "Доброе утро! 🌞 \nПопейте,ожалуйста, воду!")

schedule.every().day.at("08:00").do(good_mo)

def good_day():
    bot.send_message(message.from_user.id, "Время обеда, а, значит, пора пить воду! 🕑 ")

schedule.every().day.at("14:00").do(good_day)

def good_ev():
    bot.send_message(message.from_user.id, "Вечером тоже нужно пить воду! 💗 ")

schedule.every().day.at("20:00").do(good_ev)

def good_ni():
    bot.send_message(message.from_user.id, "Доброй ночи! 🌙 \nПопейте, перед сном, пожалуйста! ")

schedule.every().day.at("22:00").do(good_ni)

while True:
    schedule.run_pending()
    time.sleep(1)
