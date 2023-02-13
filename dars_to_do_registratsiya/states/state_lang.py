from aiogram.dispatcher.filters.state import State, StatesGroup


class Language(StatesGroup):
    uzbek = State()
    russian = State()
    english = State()