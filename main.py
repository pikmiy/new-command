import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot= Bot(token=TOKEN)
dp= Dispatcher()



async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
