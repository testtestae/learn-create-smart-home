import telebot
from telebot import types
from main import stack
bot = telebot.TeleBot('5101915679:AAH5dQUtxk46aURn5H6R4RIKIX2bAxGmbLo')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Команды")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Приветствую, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Команды"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Включи чайник")
        btn2 = types.KeyboardButton("Выключи чайник")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Что мне сделать?", reply_markup=markup)
    elif (message.text == "Включи чайник"):
        bot.send_message(message.chat.id, "Включаю")
    elif message.text == "Выключи чайник":
        bot.send_message(message.chat.id, text="Выключаю")
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Команды")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Для начала работы напишите команду /start")


def telegram_start():
    bot.polling(none_stop=True)