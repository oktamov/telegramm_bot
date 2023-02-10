import json
import logging
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand

API_TOKEN = '6072146537:AAHiGDmDZ4EKfSGWk9Jj8Hr5QS3A1dmEM5c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Command(['start', 'help']))
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Weather bot!\nPowered by @developer2006.")


@dp.message_handler(Command("weather"))
async def menu_command(message: Message):
    await message.answer("kunni tanlang", reply_markup=menu)


@dp.message_handler(text="Feb 9")
async def feb_9(message: Message):
    with open("date.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        avg_temp = jsonObject[0]["average_temperature"]
        msg = f"9 - fevraldagi ob_havo:\nHarorat: {avg_temp}"
    await message.answer(msg)


@dp.message_handler(text="Feb 10")
async def feb_10(message: Message):
    with open("date.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        avg_temp = jsonObject[1]["average_temperature"]
        msg = f"10 - fevraldagi ob_havo:\nHarorat: {avg_temp}"
    await message.answer(msg)


@dp.message_handler(text="Feb 11")
async def feb_10(message: Message):
    with open("date.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        avg_temp = jsonObject[2]["average_temperature"]
        msg = f"11 - fevraldagi ob_havo:\nHarorat: {avg_temp}"
    await message.answer(msg)


@dp.message_handler(text="Feb 12")
async def feb_10(message: Message):
    with open("date.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        avg_temp = jsonObject[3]["average_temperature"]
        msg = f"12 - fevraldagi ob_havo:\nHarorat: {avg_temp}"
    await message.answer(msg)


@dp.message_handler(text="Feb 13")
async def feb_10(message: Message):
    with open("date.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        avg_temp = jsonObject[1]["average_temperature"]
        msg = f"13 - fevraldagi ob_havo:\nHarorat: {avg_temp}"
    await message.answer(msg)


async def set_default_commands(disp):
    bot_commands=[
        types.BotCommand("start", "Ishga tushirish"),
        types.BotCommand("help", "Yordam"),
        types.BotCommand("weather", "Ob-havo")

    ]
    await bot.set_my_commands(bot_commands)



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Feb 9'),
            KeyboardButton(text='Feb 10'),
            KeyboardButton(text='Feb 11'),
            KeyboardButton(text='Feb 12'),
            KeyboardButton(text='Feb 13')

        ],
    ],
    resize_keyboard=True
)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_default_commands)
