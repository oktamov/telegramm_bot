import logging

import requests as requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from states import Kurs

API_TOKEN = '5437826398:AAG92sIMEoBP5PudVMV4zYhIJQtbGnm3uV0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Command(['start', 'help']))
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("From valyuta:", reply_markup=menu)


@dp.message_handler(text="UZS-USD")
async def from_uzs(message: Message):
    await message.answer("kiriting:")
    await Kurs.uzs_usd.set()


@dp.message_handler(state=Kurs.uzs_usd)
async def from_uzs_(message: Message, state: FSMContext):
    url = f"https://api.exchangerate-api.com/v4/latest/UZS"
    response = requests.get(url)
    data = response.json()
    result = data['rates']['USD']
    if message.text in ["USD-UZS", "RUB-UZS", "RUB-USD", "UZS-RUB", "USD-RUB"]:
        await state.finish()
    else:
        result = float(result) * float(message.text)
        await message.answer(f"UZS {message.text} = USD {result}")


@dp.message_handler(text="USD-UZS")
async def from_usd(message: Message):
    await message.answer("kiriting:")
    await Kurs.usd_uzs.set()


@dp.message_handler(state=Kurs.usd_uzs)
async def from_usd_(message: Message, state: FSMContext):
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    result = data['rates']['UZS']
    if message.text in ["UZS-USD", "RUB-UZS", "RUB-USD", "UZS-RUB", "USD-RUB"]:
        await state.finish()
    else:
        result = float(result) * float(message.text)
        await message.answer(f"USD {message.text} = UZS {result}")


@dp.message_handler(text="RUB-UZS")
async def from_rub(message: Message):
    await message.answer("kiriting:")
    await Kurs.rub_uzs.set()


@dp.message_handler(state=Kurs.rub_uzs)
async def from_rub(message: Message, state: FSMContext):
    url = f"https://api.exchangerate-api.com/v4/latest/RUB"
    response = requests.get(url)
    data = response.json()
    result = data['rates']['UZS']
    if message.text in ["UZS-USD", "USD-UZS", "RUB-USD", "UZS-RUB", "USD-RUB"]:
        await state.finish()
    else:
        result = float(result) * float(message.text)
        await message.answer(f"RUB {message.text} = UZS {result}")


@dp.message_handler(text="RUB-USD")
async def rub_usd(message: Message):
    await message.answer("kiriting:")
    await Kurs.rub_usd.set()


@dp.message_handler(state=Kurs.rub_usd)
async def rub_usd(message: Message, state: FSMContext):
    url = f"https://api.exchangerate-api.com/v4/latest/RUB"
    response = requests.get(url)
    data = response.json()
    result = data['rates']['USD']
    if message.text in ["UZS-USD", "USD-UZS", "RUB-UZS", "UZS-RUB", "USD-RUB"]:
        await state.finish()
    else:
        result = float(result) * float(message.text)
        await message.answer(f"RUB {message.text} = USD {result}")


@dp.message_handler(text="UZS-RUB")
async def rub_uzs(message: Message):
    await message.answer("kiriting:")
    await Kurs.uzs_rub.set()


@rub_uzs
@dp.message_handler(state=Kurs.uzs_rub)
async def rub_uzs(message: Message, state: FSMContext):
    url = f"https://api.exchangerate-api.com/v4/latest/UZS"
    response = requests.get(url)
    data = response.json()
    result = data['rates']['RUB']
    result = float(result) * float(message.text)
    await message.answer(f"UZS {message.text} = RUB {result}")
    if message.text in ["UZS-USD", "USD-UZS", "RUB-UZS", "RUB-USD", "USD-RUB"]:
        await state.finish()


@dp.message_handler(text="USD-RUB")
async def usd_rub(message: Message):
    await message.answer("kiriting:")
    await Kurs.usd_rub.set()


@usd_rub
@dp.message_handler(state=Kurs.usd_rub)
async def usd_rub(message: Message, state: FSMContext):
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    result = data['rates']['USD']
    if message.text in ["UZS-USD", "USD-UZS", "RUB-UZS", "RUB-USD", "UZS-RUB"]:
        await state.finish()
    else:
        result = float(result) * float(message.text)
        await message.answer(f"USD {message.text} = RUB {result}")


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="UZS-USD"),
            KeyboardButton(text="USD-UZS"),
            KeyboardButton(text="RUB-UZS"),
            KeyboardButton(text="RUB-USD"),
            KeyboardButton(text="UZS-RUB"),
            KeyboardButton(text="USD-RUB")
        ],
    ],
    resize_keyboard=True
)

menu_ortga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start")
        ],
    ],
    resize_keyboard=True
)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
