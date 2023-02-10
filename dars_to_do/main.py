import csv
import logging
import os

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import Personaldata

API_TOKEN = '6208044146:AAE-R6Fawna57X2t3Ix8U6ZnCSygMsHvdZI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm TO-DO bot")


@dp.message_handler(Command('register'))
async def register(message: types.Message):
    await message.answer("Enter full name:")
    await Personaldata.fullname.set()


@dp.message_handler(state=Personaldata.fullname)
async def fullname(message: types.Message, state: FSMContext):
    fullName = message.text
    await state.update_data(
        {"name": fullName}
    )

    await message.answer("Yoshingizni kiriting:")
    await Personaldata.next()


@dp.message_handler(state=Personaldata.age)
async def age_calc(message: types.Message, state: FSMContext):
    age_ = message.text
    await state.update_data(
        {"age": age_}
    )

    await Personaldata.phone.set()
    await message.answer("telefon raqamingiz:", reply_markup=menu_cont)


@dp.message_handler(content_types="contact", state=Personaldata.phone)
async def phone(message: types.Message, state: FSMContext):
    phone_num = message.contact.phone_number
    await state.update_data(
        {"phone": phone_num}
    )
    await message.answer("manzilingizni kiriting:", reply_markup=None)
    await Personaldata.next()


@dp.message_handler(state=Personaldata.address)
async def address(message: types.Message, state: FSMContext):
    addres = message.text
    await state.update_data(
        {"address": addres}
    )
    await message.answer("You are gender?", reply_markup=menu_gender)
    await Personaldata.next()


@dp.message_handler(lambda message: message.text in ["Male", "Female"], state=Personaldata.gender)
async def get_gender(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(
        {"gender": gender}
    )

    data = await state.get_data()
    csv_data = []
    name = data.get("name")
    csv_data.append(name)
    age = data.get("age")
    csv_data.append(age)
    phone = data.get("phone")
    csv_data.append(phone)
    address = data.get("address")
    csv_data.append(address)
    gender = data.get("gender")
    csv_data.append(gender)
    print(csv_data)
    with open("users.csv", 'a', newline="\n") as f:
        header = ['fullname', "age", "phone", "address", "gender"]
        dict_writer = csv.writer(f)
        if os.path.getsize('users.csv') == 0:
            dict_writer.writerow(header)
        dict_writer.writerow(csv_data)

    msg = f"Ism: {name}\n"
    msg += f"Yoshi: {age}\n"
    msg += f"telefon: {phone}\n"
    msg += f"Address: {address}"
    await message.answer(msg)

    await state.finish()


menu_cont = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

menu_gender = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Male"),
            KeyboardButton(text="Female")
        ],
    ],
    resize_keyboard=True
)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
