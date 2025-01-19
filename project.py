import telebot

from .config import token
bot=telebot.telebot(token)
a = 100

@bot.message_handler(commands=['start'])
def start-message(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("Вариант 1", callback_data="Вариант1")
    button2 = telebot.types.InlineKeyboardButton("Вариант 2", callback_data="Вариант2")


    markup.add(button1, button2)
    bot.send-message(message.chat.id,"Привет 👋" markup = markup)

@bot.callback_query_handler(func=lambda call.data == 'Вариант1')
def save_btn(call):
        bot.send_message(call.message.chat.id, "Вариант 1")
@bot.callback_query_handler(func=lambda call.data == 'Вариант2')
def save_btn(call):
        bot.send_message(call.message.chat.id, "Вариант 2")




    bot.infinity_polling()