from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5993209946:AAH9D3vWoe_OdevnlVR5xkrQaDPLfk0WXdI')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web', web_app=WebAppInfo(url='https://file:///C:/Users/User/Desktop/py/index.html')))
    await message.answer('H', reply_markup=markup)





executor.start_polling(dp)

