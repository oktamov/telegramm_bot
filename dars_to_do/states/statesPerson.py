from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalUzb(StatesGroup):
    fullname = State()
    age = State()
    phone = State()
    address = State()
    gender = State()


class PersonalRu(StatesGroup):
    ru_fullname = State()
    ru_age = State()
    ru_phone = State()
    ru_address = State()
    ru_gender = State()


class PersonalEng(StatesGroup):
    fullname = State()
    age = State()
    phone = State()
    address = State()
    gender = State()




