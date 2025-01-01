# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# # Bot tokenini o'rnating
# TOKEN = '8117938061:AAFMNrIP4HWansJJG9D3pkNDKo3nNAsreTA'
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Bmw"), KeyboardButton(text="Bugatti")],
#         [KeyboardButton(text="Chevrolet"), KeyboardButton(text="Audi")],
#     ],
#     resize_keyboard=True
# )
#
#
# MEDIA = {
#     "Bmw": {
#         "photo": "https://t3.ftcdn.net/jpg/04/35/92/40/360_F_435924070_A2n5ZyQUF7nCRsYZj6SX1SAYOn5sggFh.jpg",
#         "video": "https://videos.pexels.com/video-files/8552238/8552238-sd_640_360_30fps.mp4",
#     },
#     "Bugatti": {
#         "photo": "https://t3.ftcdn.net/jpg/05/59/69/60/360_F_559696075_8cA9UO2Vtuzld0fibp9h35MsAELpMPZW.jpg",
#         "video": "https://videocdn.cdnpk.net/euphony/content/video/partners1036/large_watermarked/BB_f0873707-7610-4201-a247-c26bf4b7f2b9_preview.mp4",
#     },
#     "Chevrolet": {
#         "photo": "https://www.topgear.com/sites/default/files/cars-car/image/2019/01/2018-sema-chevrolet-camaro-shock-020.jpg",
#         "video": "https://videos.pexels.com/video-files/27257029/12103861_360_640_30fps.mp4",
#     },
#     "Audi": {
#         "photo": "https://stimg.cardekho.com/images/carexteriorimages/930x620/Audi/A5/11864/1721137944455/front-left-side-47.jpg",
#         "video": "https://videos.pexels.com/video-files/18296880/18296880-uhd_2730_1440_50fps.mp4",
#     },
# }
#
#
# @dp.message(Command("start"))
# async def start_command(message: types.Message):
#     await message.answer("Iltimos, birini tanlang:", reply_markup=keyboard)
#
#
# @dp.message()
# async def handle_button_press(message: types.Message):
#     car = message.text
#     if car in MEDIA:
#         media = MEDIA[car]
#         photo_url = media["photo"]
#         video_url = media["video"]
#
#         await message.reply_photo(photo_url, caption=f"Siz tanlagan avtomobilning rasmi: {car}")
#         await message.reply_video(video_url, caption=f"Siz tanlagan avtomobil videosi: {car}")
#     else:
#         await message.reply("Noma'lum tugma tanlandi!")
#
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())




















# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile
#
# # Bot tokenini o'rnating
# TOKEN = '8117938061:AAFMNrIP4HWansJJG9D3pkNDKo3nNAsreTA'
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# # Asosiy menyu uchun klaviatura (avtomobillar)
# main_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Bmw"), KeyboardButton(text="Bugatti")],
#         [KeyboardButton(text="Chevrolet"), KeyboardButton(text="Audi")],
#     ],
#     resize_keyboard=True
# )
#
# # BMW submenyusi uchun klaviatura
# bmw_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Bmw i5"), KeyboardButton(text="Bmw x3")],
#         [KeyboardButton(text="Bmw i3"), KeyboardButton(text="Bmw x7")],
#         [KeyboardButton(text="Orqaga")],
#     ],
#     resize_keyboard=True
# )
# bugatti_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Bugatti chiron"), KeyboardButton(text="Bugatti veyron")],
#         [KeyboardButton(text="Bugatti Divo"), KeyboardButton(text="Bugatti Eb110")],
#         [KeyboardButton(text="Orqaga")],
#     ],
#     resize_keyboard=True
# )
# chevrolet_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Chevrolet Camaro"), KeyboardButton(text="Chevrolet Malibu")],
#         [KeyboardButton(text="Chevrolet Damas"), KeyboardButton(text="Chevrolet Corvette")],
#         [KeyboardButton(text="Orqaga")],
#     ],
#     resize_keyboard=True
# )
# audi_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Audi a5"), KeyboardButton(text="Audi r8")],
#         [KeyboardButton(text="Audi E-tron"), KeyboardButton(text="Audi rs5")],
#         [KeyboardButton(text="Orqaga")],
#     ],
#     resize_keyboard=True
# )
#
# # Foydalanuvchi holati
# user_states = {}
#
#
# @dp.message(Command("start"))
# async def start_command(message: types.Message):
#     # Foydalanuvchini asosiy menyu holatiga o'rnatamiz
#     user_states[message.from_user.id] = "main_menu"
#     await message.answer("Iltimos, avtomobillardan birini tanlang:", reply_markup=main_menu)
#
#
# @dp.message()
# async def handle_message(message: types.Message):
#     user_id = message.from_user.id
#     text = message.text
#
#     # Foydalanuvchi asosiy menyuda bo'lsa
#     if user_states.get(user_id) == "main_menu":
#         if text == "Bmw":
#             user_states[user_id] = "bmw_menu"
#             await message.answer("BMW modellaridan birini tanlang:", reply_markup=bmw_menu)
#         elif text == "Bugatti":
#             user_states[user_id] = "bugatti_menu"
#             await message.answer("Bugatti modellaridan birini tanlang:", reply_markup=bugatti_menu)
#         elif text == "Chevrolet":
#             user_states[user_id] = "chevrolet_menu"
#             await message.answer("Chevrolet modellaridan birini tanlang:", reply_markup=chevrolet_menu)
#         elif text == "Audi":
#             user_states[user_id] = "audi_menu"
#             await message.answer("Audi modellaridan birini tanlang:", reply_markup=audi_menu)
#         else:
#             await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")
#
#     # Foydalanuvchi BMW menyusida bo'lsa
#     elif user_states.get(user_id) == "bmw_menu":
#         if text in ["Bmw i5", "Bmw x3", "Bmw i3", "Bmw x7"]:
#             await send_bmw_details(message, text)
#         elif text == "Orqaga":
#             user_states[user_id] = "main_menu"
#             await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
#         else:
#             await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")
#     elif user_states.get(user_id) == "bugatti_menu":
#         if text in ["Bugatti chiron", "Bugatti veyron", "Bugatti Divo", "Bugatti Eb110"]:
#             await message.reply(f"{text} modelini tanladingiz!")
#         elif text == "Orqaga":
#             user_states[user_id] = "main_menu"
#             await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
#         else:
#             await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")
#
#     elif user_states.get(user_id) == "chevrolet_menu":
#         if text in ["Chevrolet Camaro", "Chevrolet Malibu", "Chevrolet Damas", "Chevrolet Corvette"]:
#             await message.reply(f"{text} modelini tanladingiz!")
#         elif text == "Orqaga":
#             user_states[user_id] = "main_menu"
#             await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
#         else:
#             await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")
#
#     elif user_states.get(user_id) == "audi_menu":
#         if text in ["Audi a5", "Audi r8", "Audi E-tron", "Audi rs5"]:
#             await message.reply(f"{text} modelini tanladingiz!")
#         elif text == "Orqaga":
#             user_states[user_id] = "main_menu"
#             await message.answer("Asosiy menyuga qaytdingiz:", reply_markup=main_menu)
#         else:
#             await message.reply("Iltimos, menyudagi tugmalardan birini tanlang!")
#
#
# import os
# from aiogram.types import InputFile
#
# async def send_bmw_details(message, model):
#     # Modelga ko'ra rasm, video va tekst
#     car_data = {
#         "Bmw i5": {
#             "text": "BMW i5 - Elektromobil oilasining zamonaviy modeli.",
#             "photo": "images/bmw_i5.jpg",
#             "video": "videos/bmw_i5.mp4"
#         },
#         "Bmw x3": {
#             "text": "BMW X3 - Oilaviy SUV avtomobili, keng va kuchli.",
#             "photo": "images/bmw_x3.jpg",
#             "video": "videos/bmw_x3.mp4"
#         },
#         "Bmw i3": {
#             "text": "BMW i3 - Shaharda yurish uchun ideal kichik elektromobil.",
#             "photo": "images/bmw_i3.jpg",
#             "video": "videos/bmw_i3.mp4"
#         },
#         "Bmw x7": {
#             "text": "BMW X7 - Luks klassdagi eng katta SUV avtomobil.",
#             "photo": "images/bmw_x7.jpg",
#             "video": "videos/bmw_x7.mp4"
#         }
#     }
#     data = car_data.get(model)
#     if not data:
#         await message.reply("Bu model haqida ma'lumot topilmadi.")
#         return
#
#     photo_path = os.path.abspath(data["photo"])
#
#     # Fayl mavjudligini tekshirish
#     if not os.path.exists(photo_path):
#         await message.reply(f"Fayl topilmadi: {photo_path}")
#         return
#
#     # Rasmni yuborish
#     photo = InputFile(photo_path)
#     await message.answer_photo(photo, caption=data["text"])
#
#
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())