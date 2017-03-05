# -*- coding: utf-8 -*-
import random
import string
import config
import telebot

bot = telebot.TeleBot(config.token)

def fun(n):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, fun(8))

if __name__ == '__main__':
     bot.polling(none_stop=True)

