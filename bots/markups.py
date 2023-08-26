from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

btnMain = KeyboardButton('⬅ Главное меню')


# Главное меню
btnBuy = KeyboardButton('💰 Купить')
btnInfo = KeyboardButton('ℹ Подробнее')
btnInfoGame = KeyboardButton('ℹ Об Игре')
btndop = KeyboardButton('↪ Дополнительно')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBuy, btnInfo, btnInfoGame, btndop)


# Меню + факты
btnmenu = KeyboardButton('⬅ Меню')
b1 = KeyboardButton('Мираж')
b2 = KeyboardButton('Онрё')
b3 = KeyboardButton('Банши')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(b3, b1, b2, btnmenu)



# Админ панель
mainpanel = ReplyKeyboardMarkup(resize_keyboard=True)
btnadm = KeyboardButton('Админ-Панель')
mainpanel = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBuy, btnInfo, btnInfoGame, btndop).add(btnadm)

adminpanel = ReplyKeyboardMarkup(resize_keyboard=True)
adminpanel.add('Добавить товар', 'Удалить товар').add('Сделать рассылку').add('⬅ Меню')





# b1 = KeyboardButton('Купить')
# b2 = KeyboardButton('Подробнее')
# b3 = KeyboardButton('Об Игре')
# b4 = KeyboardButton('Дополнительно')


# Тестовые кнопки
# bt1 = KeyboardButton('Open steam')


# markup = ReplyKeyboardMarkup(resize_keyboard=True)

# markup.add(b1)
# markup.row(b2, b3)

