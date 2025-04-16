import os
import telebot

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Убираем Webhook
bot.remove_webhook()

# Запускаем polling
bot.polling(none_stop=True)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот для Федерации Эстетической Гимнастики Курска!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True)