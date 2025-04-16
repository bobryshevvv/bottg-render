from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен, который ты получил от BotFather
API_TOKEN = 8005566639:AAHgfTudSiSR-v7I2DI7PYQ1ZAoyxy3cJjA

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой бот.')

def main():
    # Создаём объект Updater с твоим токеном
    updater = Updater(API_TOKEN, use_context=True)

    # Получаем диспетчер для добавления обработчиков
    dispatcher = updater.dispatcher

    # Добавляем обработчик для команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
