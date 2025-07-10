from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("John Galt Dashboard Bot активен!")

async def low_stock_alert(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id="@your_channel", text="Низкий уровень товара!")

def run_bot():
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.job_queue.run_repeating(low_stock_alert, interval=3600, first=0)
    app.run_polling()

if __name__ == "__main__":
    run_bot()
