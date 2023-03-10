import telebot
import urllib.request
from pydub import AudioSegment

BOT_TOKEN = "6190777383:AAFK0RNBkoj1AuDYBbcAiC6TVLuSSetQWZg"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! I am convert image to text\n'
                          'send photo')


def download_voice(messag):
    file_info = bot.get_file(messag.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)


def convert_voice():
    sound = AudioSegment.from_file('voice.ogg', format='ogg')
    sound.export('audio.mp3', format='mp3')


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    file_id = message.voice.file_id
    file_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}'
    bot.send_message(message.chat.id, file_url)
    urllib.request.urlretrieve(file_url, f'{file_id}.oga')

    # with open(f'{file_info}.ogg', 'wb') as f:
    #     f.write(downloaded_file)

    sound = AudioSegment.from_file(f'{file_id}.oga', format='oga')
    sound.export(f'{file_id}.mp3', format='mp3')

    with open(f'{file_id}.mp3', 'rb') as f:
        bot.send_audio(message.chat.id, f)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, 'Hello! I am convert image to text\n'
                                      'send photo\nadmin: @developer2006')


if __name__ == "__main__":
    print("started")
    bot.infinity_polling()
