import telebot
import os
from PIL import Image
import pytesseract

bot = telebot.TeleBot('6182467188:AAFQPq1L1PCZ57NPb-q9OOcDlrToG7-xmrU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! I am convert image to text\n'
                          'send photo')


@bot.message_handler(content_types=['photo'])
def photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f'{file_id}.jpg', 'wb') as f:
        f.write(downloaded_file)
    img = Image.open(f"{file_id}.jpg")
    pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(img)
    bot.send_message(message.chat.id, text)
    if os.path.exists(f'{file_id}.jpg'):
        os.remove(f'{file_id}.jpg')

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, 'Hello! I am convert image to text\n'
                          'send photo\nadmin: @developer2006')

if __name__ == "__main__":
    print("started")
    bot.infinity_polling()
