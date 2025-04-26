import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Tokenni o'zgartiring
API_TOKEN = '7770378906:AAG14hcuuCZz5K3eAGFg4aEEGzn2psql4yM'

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Botni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start komandasi uchun handler
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Salom! Men echo botiman. Yozganingizni qaytarib beraman!")

# Boshqa barcha xabarlarni qaytarish (echo)
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

# Botni ishga tushirish
async def on_start():
    await dp.start_polling(bot)

# Asinxron ishga tushirish
if __name__ == "__main__":
    asyncio.run(on_start())
