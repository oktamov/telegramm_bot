from aiogram.dispatcher.filters.state import StatesGroup, State

class Kurs(StatesGroup):
    uzs_usd = State()
    usd_uzs = State()
    rub_uzs = State()
    rub_usd = State()
    uzs_rub = State()
    usd_rub = State()
