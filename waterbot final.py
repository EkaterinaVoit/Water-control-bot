import telebot
import datetime
from datetime import datetime
from telebot import types
import schedule
import time
import os
from subprocess import call
import sys

bot = telebot.TeleBot("1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg")
TOKEN = '1506364107:AAHCWzAP0Vov1DH8fuSZom_UXcTy5MvzHUg'
bot = telebot.TeleBot(TOKEN)
picture1 = "https://i.pinimg.com/originals/dc/24/f4/dc24f4dd8487e2e391084c9ae5004451.jpg"
picture2 = "https://i.pinimg.com/originals/5b/83/70/5b83707a6732fcce90b1b571207f9ea8.jpg"

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtn1 = types.KeyboardButton('Да🤗')
itembtn2 = types.KeyboardButton('Нет😔')
markup.add(itembtn1, itembtn2)


morkov = types.ReplyKeyboardMarkup(resize_keyboard=True)
vremya1 = types.KeyboardButton('18:00')
vremya2 = types.KeyboardButton('19:00')
vremya3 = types.KeyboardButton('20:00')
vremya4 = types.KeyboardButton('21:00')
morkov.row(vremya1, vremya2, vremya3, vremya4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
        if message.text == '/start':
                bot.reply_to(message, "Привет! Я бот, который поможет тебе поддерживать водный баланс! ")
                bot.send_message(message.from_user.id, "Вы готовы начать?", reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message.from_user.id, "Если Вы нажали на данную кнопку, значит Вам нужна помощь!\nЗачем я нужен? — Я нужен для того, чтобы Вам было удобнее сохранять водный баланс!\nКак меня запустить? — Просто выберите команду '/start' или же введите ее собственноручно!\nЖелаю Вам приятного использования Бота!")
                     
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Да🤗':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, "Отлично, начинаем!", reply_markup=a) #запустить код времени
        bot.send_message(message.from_user.id, "Выберите, пожалуйста, время, когда Бот будет присылать Вам вопрос:", reply_markup=morkov)
    elif message.text == 'Нет😔':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Вы меня огорчаете(', reply_markup=a)
    elif message.text == '18:00':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Время успешно выбрано!', reply_markup=a) #запустить код конкретного времени
        call(["python", "six hours.py", str(message.from_user.id)])
    elif message.text == '19:00':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Время успешно выбрано!', reply_markup=a) #запустить код конкретного времени
        call(["python", "seven hours.py", str(message.from_user.id)])
    elif message.text == '20:00':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Время успешно выбрано!', reply_markup=a) #запустить код конкретного времени
        call(["python", "eight hours.py", str(message.from_user.id)])
    elif message.text == '21:00':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Время успешно выбрано!', reply_markup=a) #запустить код конкретного времени
        call(["python", "nine hours.py", str(message.from_user.id)])
    elif message.text == 'Да👍':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Вы супер!(づ ◕‿◕ )づ', reply_markup=a)
        bot.send_photo(message.from_user.id, picture1)
    elif message.text == 'Нет👎':
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Попейте, пожалуйста!', reply_markup=a)
        bot.send_photo(message.from_user.id, picture2)
        
bot.polling()

