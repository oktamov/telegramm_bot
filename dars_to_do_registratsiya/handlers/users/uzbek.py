import csv
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.default.person import menu_cont, menu_uz_gender, menu_register
from keyboards.inline.languages import menu_kurs, menu_fanlar, ha_yoq
from loader import dp
from states.statesPerson import PersonalUzb
from states.state_lang import Language


@dp.callback_query_handler(text='uz')
async def lang_uz(call: CallbackQuery):
    text = "Siz O'zbek tilini tanaladingiz.\nRo'yxatdan otish uchun /register buyrugini kiriting!"
    await call.message.answer(text)
    await Language.uzbek.set()


@dp.message_handler(Command('register'), state=Language.uzbek)
async def register(message: types.Message):
    await message.answer("Ism familiyangiz:")
    await PersonalUzb.fullname.set()


@dp.message_handler(state=PersonalUzb.fullname)
async def fullname(message: types.Message, state: FSMContext):
    fullName = message.text
    await state.update_data(
        {"name": fullName}
    )

    await message.answer("Yoshingizni kiriting:")
    await PersonalUzb.next()


@dp.message_handler(state=PersonalUzb.age)
async def age_calc(message: types.Message, state: FSMContext):
    age_ = message.text
    await state.update_data(
        {"age": age_}
    )

    await PersonalUzb.phone.set()
    await message.answer("telefon raqamingiz:", reply_markup=menu_cont)


@dp.message_handler(content_types="contact", state=PersonalUzb.phone)
async def phone(message: types.Message, state: FSMContext):
    phone_num = message.contact.phone_number
    await state.update_data(
        {"phone": phone_num}
    )
    await message.answer("manzilingizni kiriting:\nex:(Toshkent shahar, Olmozor tumani",
                         reply_markup=ReplyKeyboardRemove())
    await PersonalUzb.next()


@dp.message_handler(state=PersonalUzb.address)
async def address(message: types.Message, state: FSMContext):
    addres = message.text
    await state.update_data(
        {"address": addres}
    )
    await message.answer("Jinsingiz?", reply_markup=menu_uz_gender)
    await PersonalUzb.next()


@dp.message_handler(lambda message: message.text in ["Erkak", "Ayol"], state=PersonalUzb.gender)
async def get_gender(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(
        {"gender": gender}
    )

    data = await state.get_data()
    global csv_data
    csv_data = []
    name = data.get("name")
    csv_data.append(name)
    age = data.get("age")
    csv_data.append(age)
    phone = data.get("phone")
    csv_data.append(phone)
    address = data.get("address")
    csv_data.append(address)
    gender = data.get("gender")
    csv_data.append(gender)


    msg = f"Ism familiya: {name}\n"
    msg += f"Yoshi: {age}\n"
    msg += f"telefon: {phone}\n"
    msg += f"Manzil: {address}\n"
    msg += f"Jinsi: {gender}"
    await message.answer(msg, reply_markup=menu_register)

    await state.finish()


@dp.message_handler(text="Kurslar💻")
async def kurslar(message: types.Message):
    await message.answer("qay tarzda oqiysiz?", reply_markup=menu_kurs)


@dp.callback_query_handler(text='offline')
async def fanlar(call: CallbackQuery):
    await call.message.answer("kurslarimiz:", reply_markup=menu_fanlar)


@dp.callback_query_handler(text='foundation')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 2 modul\nKURSIMIZ KIMLARGA TO’G’RI KELADI:\n"
                              "0 dan boshlamoqchi bo’lganlarga - Dasturlash sohasi bo’yicha hech qanday bilimga ega bo’lmagan har qanday inson dasturlash saboqlarini o’rganishi mumkin\n"
                              "Boshlang’ich bilimga - ega bo’lganlarga Bu kurs bo’yicha boshlang’ich bilimga ega bo’lgan bo’lajak dasturchilar o’z bilimlarini mustahkamlash orqali yuqori bosqichga olib chiqish imkoniyatiga egadirlar")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)

@dp.callback_query_handler(text='python')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 7 modul\nPython Backend Roadmap Yo’nalishlari Python bu kelajak dasturlash tili bo’lib, kelajakda u insonlarga ulkan,"
                              " ishonchli, samarali va tez ishlaydigan texnologiyalarni yaratishda asosiy yordamchiga aylanadi. So’nggi olib borilgan izlanishlarga ko’ra,"
                              " Python ilk bor ommaga taqdim etilgandan buyon dasturchilar o’rtasida umumiy hisobda 4,5 barobar o’sish ko’rsatgichini va dasturlash olamiga "
                              "40.000 dan ortiq yangi ish o’rinlarini olib kira olgan til hisoblanadi.")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)


@dp.callback_query_handler(text='java')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 9 modul\nJava Backend Roadmap Yo’nalishlari Java dasturlash tili hozirgi kunda dunyoning gigant dasturlash tillaridan biri hisoblanadi."
                              " Siz bu dasturlash tilini o’rganish orqali istalgan sohada yuqori maoshli kasb egasi bo’lishingiz mumkin.")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)



@dp.callback_query_handler(text='ios')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 8 modul\niOS Roadmap Yo’nalishlari iOS - Apple Inc. tomonidan yaratilgan va ishlab chiqarilgan mobil operatsion tizimdir."
                              " Hozirda kompaniyaning ko'plab mobil qurilmalarini, jumladan, iPhone, iPad va iPod Touchni quvvatlovchi operatsion tizim.")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)


@dp.callback_query_handler(text='android')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 8 modul\nAndroid Roadmap Yo’nalishlari Mobil dasturlash sohasi hozirgi kunning"
                              " eng muhim sohalaridan biri. Bu sohani o’rganish orqali hozirda mobil qurilmalar(smartfon, planshet, watchlar)ga dasturlar yaratish imkoniga ega bo’lasiz.")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)

@dp.callback_query_handler(text='flutter')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 10 modul\nFlutter Roadmap Yo’nalishlari Flutter - Google tomonidan ishlab chiqilgan framework"
                              " hisoblanadi. Bu kurs orqali siz bir vaqtning o'zida yangi til Dart ni o`rganib Android va iOS mobil ilovalarni yarata olasiz.")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)

@dp.callback_query_handler(text='.net')
async def fanlar(call: CallbackQuery):
    await call.message.answer("Davomiyligi: 9 modul\n.NET Backend Roadmap Yo’nalishlari C# dasturlash tili - obyektga yo’naltirilgan, zamonaviy dasturlash tili hisoblanib,"
                              " dasturchilarga .NET platformasida ishga tushuvchi xavfsiz va mustahkam dasturlar qurishda qo’l keladi.")
    await call.message.answer("Kursimizdan royxatdan otasizmi?", reply_markup=ha_yoq)


@dp.callback_query_handler(text='ha')
async def ha_yoq_func(call: CallbackQuery):
    await call.message.answer("Siz bilan tez orada mutahasislarimiz boglanadi.")
    global csv_data
    with open("users.csv", 'a', newline="\n") as f:
        header = ['fullname', "age", "phone", "address", "gender"]
        dict_writer = csv.writer(f)
        if os.path.getsize('users.csv') == 0:
            dict_writer.writerow(header)
        dict_writer.writerow(csv_data)


@dp.callback_query_handler(text='yoq')
async def ha_yoq_func(call: CallbackQuery):
    await call.message.answer("so'rovnomangiz ochirib yuborildi.")