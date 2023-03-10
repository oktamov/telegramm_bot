import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

bot = Bot(token="6088901016:AAGe3OWgWRGVPSoagBYv3Xs4l1tmGhzPOPQ")
dp = Dispatcher(bot)
openai.api_key = "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"
@dp.message_handler(commands='start')
async def start(message: types.Message):

    await bot.send_message(message.chat.id, "salom")
@dp.message_handler()
async def handle_message(message: types.Message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=256
    )
    await bot.send_message(message.chat.id, response.choices[0].text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
