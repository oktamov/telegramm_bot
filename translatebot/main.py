from googletrans import Translator

import telebot


translator = Translator()



bot = telebot.TeleBot("6057131171:AAHksr9IT4mxPfYpR9l98YQnu31uJ__omOk")


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message, f"salom")


@bot.message_handler(commands=['translator'])
def weather_handler(message):
    message_lang = translator.detect(message.text)
    bot.send_message(message, message_lang)






if __name__ == '__main__':
    print("ishlayapti")
    bot.infinity_polling()

