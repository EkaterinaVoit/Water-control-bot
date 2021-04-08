import telebot
import datetime
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



def test_send_message():
        text = 'CI Test Message'
        bot = telebot.TeleBot(TOKEN)
        ret_msg = bot.send_message(user_id, text='Добрый вечер! Вы пили воду сегодня?')
        assert ret_msg.message_id
        if current_time=="13:45:00":
            test_send_message()
          
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'да':
        bot.send_message(message.from_user.id, 'Отлично! Мы готовы начать!')
        test_send_message()
    else:
        bot.send_message(message.from_user.id, 'Я буду ждать твое "да"! Может, попробуешь еще раз?')

bot.polling()
