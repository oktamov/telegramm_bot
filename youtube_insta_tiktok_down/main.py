import requests
import telebot
from pytube import YouTube
import re

BOT_TOKEN = '6081333666:AAHfCXsaVLnj5huEZXQOqX9RucAMZUBks04'

bot = telebot.TeleBot(BOT_TOKEN)


def find_urls(text):
    # URL ni topish uchun regex
    url_regex = r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
    return re.findall(url_regex, text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom!\n"
                                      "Men You tube, Instagram va tik tokdan\n"
                                      "video yuklaydigan botman\n"
                                      "menga video linkini yuboring!")


@bot.message_handler(func=lambda message: True)
def get_youtube_video(message):
    link = find_urls(message.text)
    link = link[0][0]
    if "youtube.com" in link:
        bot.send_message(message.chat.id, "yuklanmoqda..")
        from io import BytesIO
        buffer = BytesIO()
        url = YouTube(link)
        if url.check_availability() is None:
            video = url.streams.filter(file_extension='mp4').first()
            video.stream_to_buffer(buffer=buffer)
            buffer.seek(0)
            filename = url.title
            bot.send_message(message.chat.id, "uzatilmoqda..")
            bot.send_video(message.chat.id, video=buffer, caption=filename)
        else:
            bot.send_message(message.chat.id, "Xatolik")
    elif "instagram.com" in link:
        bot.send_message(message.chat.id, "yuklanmoqda..")
        url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

        querystring = {"url": f"{link}"}

        headers = {
            "X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
            "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        down_video = response.json()['media']
        bot.send_message(message.chat.id, "Uzatilmoqda..")
        bot.send_video(message.chat.id, video=down_video)
    elif "tiktok.com" in link:
        bot.send_message(message.chat.id, "yuklanmoqda..")
        url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

        querystring = {
            "url": f"{link}"}

        headers = {
            "X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
            "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        down_video = response.json()['video'][0]
        bot.send_message(message.chat.id, "Uzatilmoqda..")
        bot.send_video(message.chat.id, video=down_video)
    else:
        bot.send_message(message.chat.id, "Salom!\n"
                                          "Men You tube, Instagram va tik tokdan\n"
                                          "video yuklaydigan botman\n"
                                          "menga video linkini yuboring!")


if __name__ == "__main__":
    print("started:...")
    bot.infinity_polling()
