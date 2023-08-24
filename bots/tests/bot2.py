from aiogram import Bot, Dispatcher, executor, types
import config
from keyboards import markup
import os

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Select button', reply_markup=markup)


@dp.message_handler(commands=['Open steam'])
async def steam(message: types.Message)
    os.open


executor.start_polling(dp)

