from aiogram.dispatcher.filters.state import State, StatesGroup


class Personaldata(StatesGroup):
    fullname = State()
    age = State()
    phone = State()
    address = State()
    gender = State()
