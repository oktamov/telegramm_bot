from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="UZ🇺🇿", callback_data="uz"),
            InlineKeyboardButton(text="RU🇷🇺", callback_data="ru"),
            InlineKeyboardButton(text="EN🇬🇧", callback_data="eng"),
        ]
    ]
)

menu_kurs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Online", url="https://online.pdp.uz/")
        ],
        [
            InlineKeyboardButton(text="Offline", callback_data='offline')
        ]
    ]
)

menu_fanlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foundation", callback_data='foundation')
        ],
        [
            InlineKeyboardButton(text="Python", callback_data='python'),
            InlineKeyboardButton(text="Java", callback_data='java'),
        ],
        [
            InlineKeyboardButton(text="IOS", callback_data='ios'),
            InlineKeyboardButton(text="Android", callback_data='android'),
        ],
        [
            InlineKeyboardButton(text="Flutter", callback_data='flutter'),
            InlineKeyboardButton(text=".NET", callback_data='.net'),
        ]
    ]
)

ha_yoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='HA', callback_data='ha'),
            InlineKeyboardButton(text='YOQ', callback_data='yoq')
        ]
    ]
)
