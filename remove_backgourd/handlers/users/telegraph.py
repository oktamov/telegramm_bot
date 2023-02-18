import io
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils import executor
from PIL import Image
import pytesseract

API_TOKEN = "5811333142:AAGz9IaWCFpP-JEKjQ0xLZSNX5ti2RgxGuI"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(content_types=['photo'])
async def process_image(message: types.Message):
    # Get file_id of the sent photo
    file_id = message.photo[-1].file_id

    # Download the photo
    file = await bot.download_file_by_id(file_id)
    print(file)
    filee = Image.open(f'{file}.jpg', 'r')
    # Open the downloaded photo using PIL
    image = Image.open(io.BytesIO(filee))

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image)

    # Send the extracted text back to the user
    await message.reply(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# import aiogram.utils
# import aiogram.utils.markdown as md
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from aiogram.bot import bot
# from aiogram.types import Message, ChatType
# from loader import dp
# from io import BytesIO
#
# from aiogram.types import ContentType, Message
#
#
# import pytesseract
# from PIL import Image
#
# @dp.message_handler(content_types=['photo'])
# async def handle_docs_photo(message: types.Message):
#
#     photo_id = await message.photo[0].download()
#     await message.answer(photo_id)
#     b = BytesIO()
#     b.write(photo_id.raw)
#     with open('testfile.jpg', 'wb') as f:
#         f.write(b.getvalue())
#     image = Image.open('testfile.png')
#     text = pytesseract.image_to_string(image)
#     await message.reply(text)
#
#
#
# @dp.message_handler(content_types=ContentType.PHOTO)
# async def extract_text(message: types.Message):
#     await message.answer("rasm yubordingiz")
#     # Get the image from the user's message
#     file_id = message.photo[-1].file_id
#     file = await (bot.download_file(file_id, 'photo.jpg'))
#     await message.answer_photo(message.chat.id, 'photo.jpg')
#
#     # Save the image to a local file
#     # with open('image.png', 'wb') as f:
#     #     f.write(image_file)
#
#     # Open the image file using PIL
#     image = Image.open('image.png')
#
#     # Extract the text from the image using Tesseract
#     text = pytesseract.image_to_string(image)
#
#     # Send the extracted text back to the user
#     print(text)
#     #await message.reply(text)
#
# #
# #
# #
# # # from aiogram import types
# # # import pytesseract
# # # from PIL import Image
# # # from loader import dp
# # # from utils import photo_link
# # # from aiogram.types import ContentType, Message
# # # from pathlib import Path
# # # from utils import get_text
# # # from utils import get_textt
# # # import urllib.request
# # #
# # #
# # # # foydalanuvchidan photo kelsa
# # # # @dp.message_handler(content_types="photo")
# # # # async def bot_echo(message: types.Message):
# # #     # # photo ozgaruvchisiga photo royxatini joylaymiz "{"file_id": "AgACAgIAAxkBAAM6Y7qaJr8_PlCDKozrpfY9gL0oyBIAAuHBMRuGAtFJ3QsFe4q-vLgBAAMCAAN5AAMtBA", "file_unique_id": "AQAD4cExG4YC0Ul-", "file_size": 45570, "width": 960, "height": 1280}")
# # #     # photo_id = message.photo[-1]
# # #     # photoo = message.photo[-1].download(photo=photo_id["file_id"])
# # #     # photo = await message.answer_photo(photo=photo_id["file_id"])
# # #     # # text = pytesseract.image_to_string(f'{photo}.png')
# # #     # await message.answer_photo(photoo)
# # # download_path = Path().joinpath("download")
# # # download_path.mkdir(parents=True, exist_ok=True)
# # #
# # #
# # # @dp.message_handler(content_types=ContentType.PHOTO)
# # # async def photo_handler(msg: Message):
# # #     #image = await msg.photo[-1].download(destination=download_path)
# # #     photo_id = msg.photo[-1].file_id
# # #     await msg.answer_photo(photo=msg.photo[-1])
# # #     #image = await msg.answer_photo(photo=photo_id)
# # #     #text = pytesseract.image_to_string(Image.open(f"{image}.png"))
# # #     #await msg.answer(image)
# # # #     # photo = msg.photo[-1]
# # # #     # img_url = await photo_link(photo)
# # # #     # await msg.reply(img_url)
# # # #     # imagee = urllib.request.urlretrieve(img_url, "image.png")
# # # #     # await msg.answer_photo(imagee)
# # # #     # text = pytesseract.image_to_string(Image.open(imagee))
# # # #     # await msg.reply(text)
