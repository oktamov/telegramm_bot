"""
This is a krill-lotin bot.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5900812181:AAEun5XvU3RfeQWT1wjdtcxZEN02qbc1LKo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm krill-lotin-krill bot")



@dp.message_handler(commands=['age'])
async def age(message: types.Message):
    await message.answer("Enter birth year:")

@dp.message_handler()
async def age_calc(message: types.Message):
    result = 2023 - int(message.text)
    await message.answer(f"yoshingiz: {result}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)