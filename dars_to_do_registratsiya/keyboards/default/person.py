from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_eng_gender = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Male"),
            KeyboardButton(text="Female")
        ],
    ],
    resize_keyboard=True
)

menu_uz_gender = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Erkak"),
            KeyboardButton(text="Ayol")
        ],
    ],
    resize_keyboard=True
)

menu_ru_gender = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Мужской"),
            KeyboardButton(text="Женский")
        ],
    ],
    resize_keyboard=True
)



menu_cont = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

menu_register = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar💻"),
            KeyboardButton(text="PDP academy")
        ],
    ],
    resize_keyboard=True
)
