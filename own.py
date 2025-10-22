import requests
from telebot import *
import os
import webbrowser
webbrowser.open('https://t.me/+Y15BGruLYzcwY2I1')


#_______________________________




token = input('ENTER YOUR TOKEN => ')


os.system('clear')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])


def s(message):
        bot.send_message(message.chat.id,text='Welcome to the SYCOxBOT')


@bot.message_handler(content_types=['text'])


def t(message):
        text = message.text.strip()
        re = requests.get(f'https://sii3.top/api/code.php?text={text}').json()
        res = re['response']
        bot.send_message(message.chat.id,res)

print('The bot was launched successfully.')

bot.polling()







