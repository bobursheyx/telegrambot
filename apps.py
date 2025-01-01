import asyncio
import statistics

from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile, InlineKeyboardMarkup, InlineKeyboardButton, \
    Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Bot tokenini o'rnating
TOKEN = '8117938061:AAFMNrIP4HWansJJG9D3pkNDKo3nNAsreTA'
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Asosiy menyu uchun klaviatura (avtomobillar)
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bmw"), KeyboardButton(text="Bugatti")],
        [KeyboardButton(text="Chevrolet"), KeyboardButton(text="Audi")],
    ],
    resize_keyboard=True
)

# BMW submenyusi uchun klaviatura
bmw_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bmw i5"), KeyboardButton(text="Bmw x3")],
        [KeyboardButton(text="Bmw i3"), KeyboardButton(text="Bmw x7")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True
)
bugatti_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bugatti chiron"), KeyboardButton(text="Bugatti veyron")],
        [KeyboardButton(text="Bugatti Divo"), KeyboardButton(text="Bugatti Eb110")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True
)
chevrolet_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Chevrolet Camaro"), KeyboardButton(text="Chevrolet Malibu")],
        [KeyboardButton(text="Chevrolet Damas"), KeyboardButton(text="Chevrolet Corvette")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True
)
audi_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Audi a5"), KeyboardButton(text="Audi r8")],
        [KeyboardButton(text="Audi E-tron"), KeyboardButton(text="Audi rs5")],
        [KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True
)

# Foydalanuvchi holati
user_states = {}

@dp.message(Command("start"))
async def start_command(message: types.Message):
    # Foydalanuvchini asosiy menyu holatiga o'rnatamiz
    user_states[message.from_user.id] = "main_menu"
    await message.answer("Iltimos, avtomobillardan birini tanlang:", reply_markup=main_menu)

@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    # Foydalanuvchi asosiy menyuda bo'lsa
    if user_states.get(user_id) == "main_menu":
        if text == "Bmw":
            user_states[user_id] = "bmw_menu"
            await message.answer("BMW modellaridan birini tanlang:", reply_markup=bmw_menu)
        elif text == "Bugatti":
            user_states[user_id] = "bugatti_menu"
            await message.answer("Bugatti modellaridan birini tanlang:", reply_markup=bugatti_menu)
        elif text == "Chevrolet":
            user_states[user_id] = "chevrolet_menu"
            await message.answer("Chevrolet modellaridan birini tanlang:", reply_markup=chevrolet_menu)
        elif text == "Audi":
            user_states[user_id] = "audi_menu"
            await message.answer("Audi modellaridan birini tanlang:", reply_markup=audi_menu)
        else:
            await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")

    # Foydalanuvchi BMW menyusida bo'lsa
    elif user_states.get(user_id) == "bmw_menu":
        if text in ["Bmw i5", "Bmw x3", "Bmw i3", "Bmw x7"]:
            await send_bmw_details(message, text)
        elif text == "Orqaga":
            user_states[user_id] = "main_menu"
            await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
        else:
            await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")
    elif user_states.get(user_id) == "bugatti_menu":
        if text in ["Bugatti chiron", "Bugatti veyron", "Bugatti Divo", "Bugatti Eb110"]:
            await send_bugatti_details(message, text)
        elif text == "Orqaga":
            user_states[user_id] = "main_menu"
            await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
        else:
            await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")

    elif user_states.get(user_id) == "chevrolet_menu":
        if text in ["Chevrolet Camaro", "Chevrolet Malibu", "Chevrolet Damas", "Chevrolet Corvette"]:
            await send_chevrolet_details(message, text)
        elif text == "Orqaga":
            user_states[user_id] = "main_menu"
            await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
        else:
            await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")

    elif user_states.get(user_id) == "audi_menu":
        if text in ["Audi a5", "Audi r8", "Audi E-tron", "Audi rs5"]:
            await send_audi_details(message, text)
        elif text == "Orqaga":
            user_states[user_id] = "main_menu"
            await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
        else:
            await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")


import os

async def send_bmw_details(message, model):
    # Modelga ko'ra rasm, video va tekst URL
    car_datattt = {
        "Bmw i5": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BMW i5 ~~~\n\n"
                "Bmw i5 Toliq tanishtirilgan video\n"
                ">>>https://youtu.be/a2yWLy2c1jQ<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Elektro\n"
                "- Quvvat, kVt (hp): 250 (340)\n"
                "- Moment, Nm: 400\n"
                "- Yuqish: 1-tezlikda, avtomatik\n"
                "- Haydash: Orqa g'ildirak haydovchisi\n\n"
                ">>>Elektr dvigateli<<<\n"
                "- Maksimal quvvat / 30 daqiqa quvvat, kVt (hp): 105 (143)\n"
                "- (Nominal) moment, Nm: 400\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 6\n"
                "- Maksimal tezlik, km/soat: 193\n"
                "- Elektr quvvatidagi maksimal tezlik, km/soat: 193\n\n"
                ">>>Iste'mol/emissiya<<<\n"
                "- Birlashgan CO2 emissiyasi WLTP, g/km: 0\n"
                "- Energiya iste'moli, birlashtirilgan WLTP, kVt/100 km: 19.5–15.9\n"
                "- Elektr diapazoni, WLTP sikli, km: 477–582\n\n"
                ">>>Yuqori kuchlanishli batareya / 48 voltli batareya, zaryadlash<<<\n"
                "- Batareya quvvati, kVt/soat: 81.2\n"
                "- 10 daqiqalik kuchli zaryaddan keyin qo'shimcha quvvat zaxirasi, km: 156\n"
                "- Maksimal zaryadlash quvvati AC kVt: 11\n"
                "- AC zaryadlash vaqti 0–100%, soat: 4:15\n"
                "- Maksimal zaryadlash quvvati DC kVt: 205\n"
                "- DC zaryadlash vaqti 10-80%, min: 30\n\n"
            ),
            "photo_url": "https://hips.hearstapps.com/hmg-prod/images/2024-bmw-i5-m60-xdrive-exterior-121-646d184e63490.jpg",
        },
        "Bmw x3": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BMW X3 ~~~\n\n"
                "BMW X3 to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/uylW8_NiQ_U<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin/Dizel/Hybrid\n"
                "- Quvvat, kVt (hp): 135-285 (184-382)\n"
                "- Moment, Nm: 350–500\n"
                "- Yuqish: 8-tezlikli avtomatik\n"
                "- Haydash: xDrive (to'liq g'ildirak) yoki sDrive (orqa g'ildirak)\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 4.9–7.3\n"
                "- Maksimal tezlik, km/soat: 210–250\n\n"
                ">>>Iste'mol/emissiya<<<\n"
                "- Birlashgan CO2 emissiyasi WLTP, g/km: 39–175\n"
                "- Yo'qilg'i iste'moli, birlashtirilgan WLTP, l/100 km: 2.0–7.5\n"
                "- Elektr diapazoni (hybrid uchun), WLTP, km: 42–50\n\n"
                ">>>Yuqori kuchlanishli batareya (Hybrid uchun)<<<\n"
                "- Batareya quvvati, kVt/soat: 12.0\n"
                "- Maksimal zaryadlash quvvati AC kVt: 7.4\n"
                "- AC zaryadlash vaqti 0–100%, soat: 3:30\n"
                "- Maksimal zaryadlash quvvati DC kVt: 50\n"
                "- DC zaryadlash vaqti 10-80%, min: 30\n\n"
            ),
            "photo_url": "https://www.edmunds.com/assets/m/cs/bltea4126eaf7ed28f9/6671ba527a609d03e8a6d32f/2025_BMW_X3_front_three_quarter_1600.jpg",
        },
        "Bmw i3": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BMW i3 ~~~\n\n"
                "Bmw i3ning to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/xh-7nElmtzU<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Elektro\n"
                "- Quvvat, kVt (hp): 125–135 (170–184)\n"
                "- Moment, Nm: 250–270\n"
                "- Yuqish: 1-tezlikli avtomatik\n"
                "- Haydash: Orqa g'ildirak haydovchisi\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 7.2–8.0\n"
                "- Maksimal tezlik, km/soat: 150–160\n\n"
                ">>>Iste'mol/emissiya<<<\n"
                "- Birlashgan CO2 emissiyasi WLTP, g/km: 0\n"
                "- Energiya iste'moli, birlashtirilgan WLTP, kVt/100 km: 14–16\n"
                "- Elektr diapazoni, WLTP sikli, km: 260–310\n\n"
                ">>>Yuqori kuchlanishli batareya<<<\n"
                "- Batareya quvvati, kVt/soat: 42.2\n"
                "- Maksimal zaryadlash quvvati DC kVt: 50\n"
                "- DC zaryadlash vaqti 10-80%, min: 30\n\n"
            ),
            "photo_url": "https://images6.alphacoders.com/123/thumb-1920-1238334.jpg",
        },
        "Bmw x7": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BMW X7 ~~~\n\n"
                "Bmw x7nig to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/zEpYQbHiYTI<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin/Dizel/Hybrid\n"
                "- Quvvat, kVt (hp): 245–390 (333–530)\n"
                "- Moment, Nm: 450–750\n"
                "- Yuqish: 8-tezlikli avtomatik\n"
                "- Haydash: xDrive (to'liq g'ildirak)\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 4.7–6.9\n"
                "- Maksimal tezlik, km/soat: 250\n\n"
                ">>>Iste'mol/emissiya<<<\n"
                "- Birlashgan CO2 emissiyasi WLTP, g/km: 39–229\n"
                "- Yo'qilg'i iste'moli, birlashtirilgan WLTP, l/100 km: 2.5–10.0\n"
                "- Elektr diapazoni (hybrid uchun), WLTP, km: 50–55\n\n"
                ">>>Yuqori kuchlanishli batareya (Hybrid uchun)<<<\n"
                "- Batareya quvvati, kVt/soat: 17.0\n"
                "- Maksimal zaryadlash quvvati AC kVt: 7.4\n"
                "- AC zaryadlash vaqti 0–100%, soat: 3:45\n"
                "- Maksimal zaryadlash quvvati DC kVt: 50\n"
                "- DC zaryadlash vaqti 10-80%, min: 30\n\n"
            ),
            "photo_url": "https://media.ed.edmunds-media.com/bmw/x7/2025/oem/2025_bmw_x7_4dr-suv_m60i_fq_oem_1_1280.jpg",
        },
    }
    data = car_datattt.get(model)
    if not data:
        await message.reply("Bu model haqida ma'lumot topilmadi.")
        return

    # Rasmlarni va videolarni havola orqali yuborish
    await message.answer_photo(data["photo_url"], caption=data["text"][:1000])


async def send_bugatti_details(message, model):
    car_datatt = {
        "Bugatti chiron": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BUGATTI CHIRON ~~~\n\n"
                "Bugatti Chiron to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/c8QXVD1qDAQ<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: W16, Quad-Turbo\n"
                "- Quvvat, kVt (hp): 1,103 (1,500)\n"
                "- Moment, Nm: 1,600\n"
                "- Yuqish: 7-tezlikli DSG\n"
                "- Haydash: To'liq g'ildirak haydovchisi\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 2.4\n"
                "- Maksimal tezlik, km/soat: 420\n\n"
                ">>>Iste'mol/emissiya<<<\n"
                "- Yo'qilg'i iste'moli, birlashtirilgan WLTP, l/100 km: 22.5\n\n"
            ),
            "photo_url": "https://www.topgear.com/sites/default/files/images/news-article/2017/08/e196eb2f1b20cd4768c7fa81f99781a8/02_us-chiron.jpg",
        },
        "Bugatti veyron": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BUGATTI VEYRON ~~~\n\n"
                "Bugatti Veyron to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/w7LmQyBag2E<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: W16, Quad-Turbo\n"
                "- Quvvat, kVt (hp): 1,001 (1,200)\n"
                "- Moment, Nm: 1,250\n"
                "- Yuqish: 7-tezlikli DSG\n"
                "- Haydash: To'liq g'ildirak haydovchisi\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 2.5\n"
                "- Maksimal tezlik, km/soat: 407\n\n"
            ),
            "photo_url": "https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1709141911/evo/2024/2/Veyron%20evo%2025.jpg",
        },
        "Bugatti Divo": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BUGATTI DIVO ~~~\n\n"
                "Bugatti Divo to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/Z8VzH4khBjI<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: W16, Quad-Turbo\n"
                "- Quvvat, kVt (hp): 1,103 (1,500)\n"
                "- Moment, Nm: 1,600\n"
                "- Yuqish: 7-tezlikli DSG\n"
                "- Haydash: To'liq g'ildirak haydovchisi\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 2.4\n"
                "- Maksimal tezlik, km/soat: 380\n\n"
            ),
            "photo_url": "https://hips.hearstapps.com/hmg-prod/images/bugatti-divo-placement-1535034871.jpg",
        },
        "Bugatti Eb110": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR BUGATTI EB110 ~~~\n\n"
                "Bugatti EB110 to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/e6V6cvE9XN4<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: V12, Quad-Turbo\n"
                "- Quvvat, kVt (hp): 450 (612)\n"
                "- Moment, Nm: 650\n"
                "- Yuqish: 6-tezlikli mexanik\n"
                "- Haydash: To'liq g'ildirak haydovchisi\n\n"
                ">>>Ishlash<<<\n"
                "- Tezlashuv 0–100 km/soat, sek: 3.2\n"
                "- Maksimal tezlik, km/soat: 355\n\n"
            ),
            "photo_url": "https://www.netcarshow.com/Bugatti-EB110_Super_Sport-1992-wallpaper.jpg",
        },
    }
    data = car_datatt.get(model)
    if not data:
        await message.reply("Bu model haqida ma'lumot topilmadi.")
        return

    # Rasmlarni va videolarni havola orqali yuborish
    await message.answer_photo(data["photo_url"],  caption=data["text"][:1000])


async def send_chevrolet_details(message, model):
    car_datat = {
        "Chevrolet Camaro": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR CHEVROLET CAMARO ~~~\n\n"
                "Chevrolet Camaro to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/q8jzRxKOGGo<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin\n"
                "- Quvvat, kVt (hp): 275–650\n"
                "- Moment, Nm: 400–880\n"
                "- Yuqish: 6-tezlikli mexanik yoki 10-tezlikli avtomatik\n"
                "- Haydash: Orqa g'ildirak haydovchisi\n\n"
            ),
            "photo_url": "https://www.cnet.com/a/img/hub/2017/02/24/b1e99e4c-829b-4a6e-b71f-b46ce984ead1/2018-chevrolet-camaro-zl1-1le-001.jpg",
        },
        "Chevrolet Malibu": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR CHEVROLET MALIBU ~~~\n\n"
                "Chevrolet Malibu to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/_yuxXdICa1s<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin\n"
                "- Quvvat, kVt (hp): 160–250\n"
                "- Moment, Nm: 250–350\n"
                "- Yuqish: 6-tezlikli avtomatik\n"
                "- Haydash: Old g'ildirak haydovchisi\n\n"
            ),
            "photo_url": "https://media.ed.edmunds-media.com/chevrolet/malibu/2025/oem/2025_chevrolet_malibu_sedan_2lt_fq_oem_1_1600.jpg",
        },
        "Chevrolet Damas": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR CHEVROLET DAMAS ~~~\n\n"
                "Chevrolet Damas to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/SFuH9WGeVFg<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin\n"
                "- Quvvat, kVt (hp): 38\n"
                "- Moment, Nm: 60\n"
                "- Yuqish: 5-tezlikli mexanik\n"
                "- Haydash: Old g'ildirak haydovchisi\n\n"
            ),
            "photo_url": "https://avtoremont.uz/thumb/2/WHxV7Jl11k18pZv43RUFLQ/580r450/d/chevrolet-damas.jpg",
        },
        "Chevrolet Corvette": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR CHEVROLET CORVETTE ~~~\n\n"
                "Chevrolet Corvette to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/EkWUiP15cfs<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin\n"
                "- Quvvat, kVt (hp): 495\n"
                "- Moment, Nm: 637\n"
                "- Yuqish: 8-tezlikli avtomatik\n"
                "- Haydash: Orqa g'ildirak haydovchisi\n\n"
            ),
            "photo_url": "https://www.topgear.com/sites/default/files/cars-car/image/2019/03/2019-chevrolet-corvette-zr1-011.jpg",
        },
    }
    data = car_datat.get(model)
    if not data:
        await message.reply("Bu model haqida ma'lumot topilmadi.")
        return

    # Rasmlarni va videolarni havola orqali yuborish
    await message.answer_photo(data["photo_url"], caption=data["text"][:1000])



async def send_audi_details(message, model):
    car_data = {
        "Audi a5": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR AUDI A5 ~~~\n\n"
                "Audi A5 to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/jVuOD5zJPbk<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Benzin/Dizel\n"
                "- Quvvat, kVt (hp): 150–367\n"
                "- Moment, Nm: 250–500\n"
                "- Yuqish: 6-tezlikli mexanik yoki 7-tezlikli S tronic\n"
                "- Haydash: Old g'ildirak yoki quattro\n\n"
            ),
            "photo_url": "https://car-images.bauersecure.com/wp-images/3649/073-audi-a5.jpg",
        },
        "Audi r8": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR AUDI R8 ~~~\n\n"
                "Audi R8 to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/ecslOXmjtm0<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: V10\n"
                "- Quvvat, kVt (hp): 570–620\n"
                "- Moment, Nm: 560\n"
                "- Yuqish: 7-tezlikli S tronic\n"
                "- Haydash: Quattro\n\n"
            ),
            "photo_url": "https://www.topgear.com/sites/default/files/2024/06/1%20Audi%20R8%20GT%20review.jpg",
        },
        "Audi E-tron": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR AUDI E-TRON ~~~\n\n"
                "Audi E-Tron to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/nDDd5YweMg0<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: Elektro\n"
                "- Quvvat, kVt (hp): 300\n"
                "- Moment, Nm: 561\n"
                "- Yuqish: 1-tezlikli avtomatik\n"
                "- Haydash: Quattro\n\n"
            ),
            "photo_url": "https://media.autoexpress.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1718640172/carbuyer/2024/06/New%20Audi%20e-tron%20GT%202024-7.jpg",
        },
        "Audi rs5": {
            "text": (
                "~~~ TEXNIK XUSUSIYATLAR AUDI RS5 ~~~\n\n"
                "Audi RS5 to'liq tanishtiruv videosi\n"
                ">>>https://youtu.be/EJeo-4dcMq4<<<\n\n"
                ">>>Umumiy uzatish<<<\n"
                "- Dvigatel turi: V6 Twin-Turbo\n"
                "- Quvvat, kVt (hp): 450\n"
                "- Moment, Nm: 600\n"
                "- Yuqish: 8-tezlikli avtomatik\n"
                "- Haydash: Quattro\n\n"
            ),
            "photo_url": "https://media.ed.edmunds-media.com/audi/rs-5/2025/oem/2025_audi_rs-5_4dr-hatchback_base_fq_oem_1_600.jpg",
        },
    }



    data = car_data.get(model)
    if not data:
        await message.reply("Bu model haqida ma'lumot topilmadi.")
        return

    # Rasmlarni va videolarni havola orqali yuborish
    await message.answer_photo(data["photo_url"], caption=data["text"][:1000])



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
