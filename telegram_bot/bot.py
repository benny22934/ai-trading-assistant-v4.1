from telegram.ext import Updater, CommandHandler
import os

def start(update, context):
    update.message.reply_text("🤖 AI Trading Bot 啟動成功！")

def start_bot():
    token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
