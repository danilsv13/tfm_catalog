from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '7933057804:AAG8bEDz9NdTAeB1LCeOQKWgoSjhFfTMShs'

def start(update: Update, context: CallbackContext):
    keyboard = [[
        InlineKeyboardButton(
            "Открыть каталог",
            web_app=WebAppInfo(url="https://tfm-catalog.vercel.app")  # временно тестим на Google
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Добро пожаловать в каталог кружек!", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
