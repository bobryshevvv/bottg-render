from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get(8005566639:AAHgfTudSiSR-v7I2DI7PYQ1ZAoyxy3cJjA)

menu_keyboard = [["Записаться", "Частые вопросы"]]
markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот Федерации эстетической гимнастики Курска.", reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Записаться":
        await update.message.reply_text("Чтобы записаться, напишите имя родителя, имя ребёнка и возраст.")
    elif text == "Частые вопросы":
        await update.message.reply_text("С 4 лет, ул. Литовская 12, тренеры: Бобрышева В.А., Королева И.А., Собенникова Е.С., группы есть бюджетные.")
    else:
        await update.message.reply_text("Не понял команду 😅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
