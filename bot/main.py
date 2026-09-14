import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 کیتاب کتابتون ته ښه راغلاست!\n\n"
        "🔎 د کتاب نوم ولیکئ، موږ به یې پیدا کړو."
    )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise RuntimeError("BOT_TOKEN is not configured")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Ketab Library Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
