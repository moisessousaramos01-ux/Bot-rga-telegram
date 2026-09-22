import os, threading, requests
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

GAME_TOKEN = os.getenv("GAME_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot RGA online 24h! Use /7d")

async def sete(update, context):
    await update.message.reply_text("Bot funcionando! Token ok.")

app_bot = Application.builder().token(TELEGRAM_TOKEN).build()
app_bot.add_handler(CommandHandler("start", start))
app_bot.add_handler(CommandHandler("7d", sete))

def run_bot():
    app_bot.run_polling()

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot RGA rodando!"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
