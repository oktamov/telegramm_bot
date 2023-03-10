import telebot
import speech_recognition as sr
import requests

bot = telebot.TeleBot("6088901016:AAGe3OWgWRGVPSoagBYv3Xs4l1tmGhzPOPQ")

@bot.message_handler(content_types=['voice'])
def handle_audio(message):
    try:
        voice = message.voice
        file_info = bot.get_file(voice.file_id)
        file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
        r = sr.Recognizer()
        with sr.AudioFile(requests.get(file_url, stream=True).raw) as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        bot.reply_to(message, f"Text: {text}")
    except Exception as e:
        bot.reply_to(message, "Failed to convert audio to text.")

if __name__ == "__main__":
    print("started")
    bot.infinity_polling()
