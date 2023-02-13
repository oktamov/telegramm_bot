import logging
from aiogram import Bot, Dispatcher, executor, types
import trello




logging.basicConfig(level=logging.INFO)



API_TOKEN = '5746361969:AAGyYLALT2QftDX3bMB-fdN9XoH60j3axqU'

# For example use simple trello client.
# You can use any Trello client instead of simple TrelloClient.
trello_client = trello.TrelloClient(api_key='8b38a7030c3dc94f6e040d80777beb38', token='43495bee8e3b7ca0a98adfd469c25e18e7327558bfde16c6f7c50ee9c9bc1c81')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['trello'])
async def cmd_trello(message: types.Message):
    boards = trello_client.list_boards()
    text = "Trello boards:\n"
    for i, board in enumerate(boards):
        text += "{}. {}\n".format(i+1, board.name)
    await bot.send_message(chat_id=message.chat.id, text=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
