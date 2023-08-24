from aiogram import Bot, Dispatcher, executor, types
import config
import markups as nav
from aiogram.types import ReplyKeyboardRemove
import random


bot = Bot(config.BOT_TOKEN) #<- Токен бота который находится в config.py
dp = Dispatcher(bot)


# Команда /start и отправка сообщения с фото + кнопками, которые находятся в папке keyboards, файл markups.py
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет! В этом боте ты можешь купить обучение для фазмы\n\n<b><i>"Зачем покупать обучение если можно посмотреть в ютубе?"</i></b>\n\nВ этом обучении рассказано все про призраков, с этим обучением можно быстро научиться определять тип призрака, а также знать все их особенности', reply_markup = nav.mainMenu, parse_mode='html')
    image = 'pha.jpg'
    file = open('./photos/' + image, 'rb')
    await bot.send_photo(message.chat.id, file)


@dp.message_handler(text=['💰 Купить'])
async def on_click(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка туториала', 'Покупка туториала по фазме', 'invoice', config.PAYMENT_TOKEN, 'RUB', [types.LabeledPrice('Покупка туториала', 200 * 100)])



@dp.message_handler(text=['ℹ Подробнее'])
async def podrobnee(message):
    await bot.send_message(message.chat.id, '<b><i>В этом туториале ты узнаешь все о призраках как:</i></b>\n\nДух   Мираж   Фантом\n\nПолтергейст   Банши   Джинн\n\nМара   Ревенант    Тень\n\nДемон   Юрэй  Они\n\nЁкай   Ханту   Горё\n\nМюлинг    Онрё    Близнецы\n\nРайдзю    Обакэ   Мимик\n\nМорой    Деоген    Тайэ', parse_mode='html')

@dp.message_handler(text=['ℹ Об Игре'])
async def infogame(message):
    await bot.send_message(message.chat.id, '<b>Phasmophobia</b> — это совместная сетевая психологическая хоррор-игра для 4 игроков. Вы и ваша команда исследователей паранормальных явлений отправитесь в места с привидениями, полные паранормальных явлений, и попытаетесь собрать как можно больше улик. Используйте свое снаряжение для охоты на призраков, чтобы найти и записать улики, чтобы продать их команде по удалению призраков.\n\n<a href="https://store.steampowered.com/app/739630/Phasmophobia/">Игра</a>', parse_mode='html')


@dp.message_handler(text=['↪ Дополнительно'])
async def dop(message):
    await bot.send_message(message.chat.id, f'Один факт о призраке:', reply_markup=nav.otherMenu)


@dp.message_handler(text=['Мираж'])
async def mirazh(message):
    await bot.send_message(message.chat.id, f'Мираж не наступает в соль')


@dp.message_handler(text=['Онрё'])
async def onre(message):
    await bot.send_message(message.chat.id, f'Онрё начинает охоту когда потушил 3 свечи')


@dp.message_handler(text=['Банши'])
async def banshi(message):
    await bot.send_message(message.chat.id, f'У банши есть уникальные крики из направленного микрофона')


@dp.message_handler(text=['⬅ Меню'])
async def menu(message):
    await bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=nav.mainMenu)


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def succes(message: types.Message):
    await message.answer(f'Успешно: {message.successful_payment.order_info}\n<a href="https://t.me/+sXmo-2umpRo3NzEy">Приватный канал</a>', parse_mode="html")



executor.start_polling(dp)

