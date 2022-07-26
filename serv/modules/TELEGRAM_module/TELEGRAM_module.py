import telebot
# from main import DEVICE_LIST
# from main import DEVICE_STATE
from telebot import types


async def TELEGRAM_module(DEVICE_LIST):
    device_list = DEVICE_LIST

    print("telebot")

    bot = telebot.TeleBot("5248823137:AAFwLNbcd2hILDcuBiJQg0pAZNitGH6wYKc")


    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Список устройств")
        markup.add(button1)
        bot.send_message(message.chat.id,"Люблю пиво".format(message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def func(message):
        if (message.text == "Список устройств"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons_list = []
            for i in device_list:
                buttons_list.append(types.KeyboardButton(i["device"]))
            [markup.add(btn) for btn in buttons_list]
            bot.send_message(message.chat.id, text="Открываю список устройств", reply_markup=markup)


    bot.polling(none_stop=True, interval=0)