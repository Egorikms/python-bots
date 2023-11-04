import telebot
import time


from telebot import types

bot = telebot.TeleBot('6523938754:AAH_RsHgULQOsdkCAnorigsfYOIaZ4msVxM')

i = 0

@bot.message_handler(commands=['start'])
def zdarova(message):
    i = 1
    while i == 1:
        bot.send_message(message.chat.id, 'Веня лох')
        bot.send_message(message.chat.id, 'Веня сосёт')


@bot.message_handler(commands=['stop'])
def stop(message):
    i = 2
    if i == 2:
        bot.stop_bot()
        i = 3

bot.polling(none_stop=True, interval=0)
