import config
import markups as nav

from aiogram import Bot, Dispatcher, executor, types
import os

bot = Bot(config.BOT_TOKEN) #<- Токен бота который находится в config.py
dp = Dispatcher(bot)


PRICE = types.LabeledPrice(label='Покупка доступа к каналу', amount=200 * 100)




# Команда /start и отправка сообщения с фото + кнопками, которые находятся в папке keyboards, файл markups.py
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет! В этом боте ты можешь купить обучение для фазмы\n\n<b><i>"Зачем покупать обучение если можно посмотреть в ютубе?"</i></b>\n\nВ этом обучении рассказано все про призраков, с этим обучением можно быстро научиться определять тип призрака, а также знать все их особенности', reply_markup = nav.mainMenu, parse_mode='html')
    image = 'pha.jpg'
    file = open('./photos/' + image, 'rb')
    await bot.send_photo(message.chat.id, file)

    if message.from_user.id == 1239637931:
        await message.answer(f'Вы авторизовались администратором', reply_markup=nav.mainpanel)

@dp.message_handler(text='Админ-Панель')
async def admin(message: types.Message):
    if message.from_user.id == 1239637931:
        await message.answer(f'Вы вошли в админ панель', reply_markup=nav.adminpanel)
    else:
        await message.answer('Такой команды нет')

# Бот отправляет запрос на покупку
@dp.message_handler(text=['💰 Купить'])
async def on_click(message: types.Message):
    await bot.send_invoice(message.chat.id,
                           title="Покупка",
                           description="Покупка доступа к каналу обучения",
                           provider_token=config.PAYMENT_TOKEN,
                           currency="rub",
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="tutorial-buy",
                           payload="test-invoice")



@dp.pre_checkout_query_handler(lambda query: True)
async def pre(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

# Успешная покупка, бот присылает ссылку на канал
@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def succes(message: types.Message):
    await message.answer(f'Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно')
    await message.answer('<a href="https://t.me/+sXmo-2umpRo3NzEy">Приватный канал</a>', parse_mode='html')



@dp.message_handler(text=['ℹ Подробнее'])
async def podrobnee(message: types.Message):
    await bot.send_message(message.chat.id, '<b><i>В этом туториале ты узнаешь все о призраках как:</i></b>\n\nДух   Мираж   Фантом\n\nПолтергейст   Банши   Джинн\n\nМара   Ревенант    Тень\n\nДемон   Юрэй  Они\n\nЁкай   Ханту   Горё\n\nМюлинг    Онрё    Близнецы\n\nРайдзю    Обакэ   Мимик\n\nМорой    Деоген    Тайэ', parse_mode='html')

@dp.message_handler(text=['ℹ Об Игре'])
async def infogame(message: types.Message):
    await bot.send_message(message.chat.id, '<b>Phasmophobia</b> — это совместная сетевая психологическая хоррор-игра для 4 игроков. Вы и ваша команда исследователей паранормальных явлений отправитесь в места с привидениями, полные паранормальных явлений, и попытаетесь собрать как можно больше улик. Используйте свое снаряжение для охоты на призраков, чтобы найти и записать улики, чтобы продать их команде по удалению призраков.\n\n<a href="https://store.steampowered.com/app/739630/Phasmophobia/">Игра</a>', parse_mode='html')


@dp.message_handler(text=['↪ Дополнительно'])
async def dop(message: types.Message):
    await bot.send_message(message.chat.id, f'Один факт о призраке:', reply_markup=nav.otherMenu)


@dp.message_handler(text=['Мираж'])
async def mirazh(message: types.Message):
    await bot.send_message(message.chat.id, f'Мираж не наступает в соль')


@dp.message_handler(text=['Онрё'])
async def onre(message: types.Message):
    await bot.send_message(message.chat.id, f'Онрё начинает охоту когда потушил 3 свечи')


@dp.message_handler(text=['Банши'])
async def banshi(message: types.Message):
    await bot.send_message(message.chat.id, f'У банши есть уникальные крики из направленного микрофона')


@dp.message_handler(text=['⬅ Меню'])
async def menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=nav.mainMenu)

    if message.from_user.id == 1239637931:
        await message.reply(f'Вы вышли в меню', reply_markup=nav.mainpanel)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)

