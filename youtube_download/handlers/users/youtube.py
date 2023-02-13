from aiogram import types
import requests
from loader import dp
from aiogram.dispatcher.filters import Text
from pytube import YouTube


@dp.message_handler(Text(startswith="https://www.youtube.com/"))
async def get_youtube_video(message: types.Message):
    await message.answer("yuklanmoqda..")
    link = message.text
    from io import BytesIO
    buffer = BytesIO()
    url = YouTube(link)
    if url.check_availability() is None:
        video = url.streams.filter(file_extension='mp4').first()
        video.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename = url.title
        await message.answer("uzatilmoqda..")
        await message.answer_video(video=buffer, caption=filename)
    else:
        await message.answer("Xatolik")


@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def get_insta_video(message: types.Message):
    await message.answer("yuklanmoqda..")
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": f"{message.text}"}

    headers = {
        "X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    down_video = response.json()['media']
    await message.answer("Uzatilmoqda..")
    await message.answer_video(video=down_video)


@dp.message_handler(Text(startswith="https://www.tiktok.com"))
async def get_insta_video(message: types.Message):
    await message.answer("yuklanmoqda..")
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {
        "url": f"{message.text}"}

    headers = {
        "X-RapidAPI-Key": "6f01dc13e8msh46da8b6a8249169p1b5857jsn3dfb408ca3e5",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    down_video = response.json()['video'][0]
    await message.answer("uzatilmoqda..")
    await message.answer_video(video=down_video)
