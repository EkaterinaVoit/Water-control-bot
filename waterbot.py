import telebot
import datetime
from datetime import datetime
from telebot import types
import schedule
import time
import os
from subprocess import call

bot = telebot.TeleBot("1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg")
TOKEN = '1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg'
bot = telebot.TeleBot(TOKEN)
chat_id= '1506364107'
user_id='485308239'

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtn1 = types.KeyboardButton('да')
itembtn2 = types.KeyboardButton('нет')
markup.add(itembtn1, itembtn2)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот, который поможет тебе поддерживать водный баланс! ")
	bot.send_message(user_id, "Вы готовы начать?", reply_markup=markup)
          
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'да':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Отлично, начинаем!', reply_markup=a) #запустить код времени
        call(["python", "raspisanie.py"])
    elif message.text.lower() == 'нет':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Вы меня огорчаете(', reply_markup=a)
    elif message.text.lower() == 'я аква-мен':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(user_id, 'Вы супер!', reply_markup=a)
    elif message.text.lower() == 'обезвоживание':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(user_id, 'не умирайте плиз', reply_markup=a)
           
bot.polling()




