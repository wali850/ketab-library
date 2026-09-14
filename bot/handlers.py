from telegram import Update
from telegram.ext import ContextTypes

from services.book_search import search_openlibrary


async def handle_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()

    if not query:
        await update.message.reply_text("🔎 مهرباني وکړئ د کتاب نوم ولیکئ.")
        return

    try:
        books = await search_openlibrary(query, limit=10)

        if not books:
            await update.message.reply_text(
                f"📚 د «{query}» لپاره کوم کتاب پیدا نه شو."
            )
            return

        message = f"🔎 د «{query}» د لټون پایلې:\n\n"

        for index, book in enumerate(books, start=1):
            title = book.get("title") or "نامعلوم"
            author = book.get("author") or "نامعلوم"
            language = book.get("language") or "نامعلوم"
            year = book.get("year") or "نامعلوم"

            message += (
                f"{index}. 📖 {title}\n"
                f"✍️ {author}\n"
                f"🌍 {language}\n"
                f"📅 {year}\n\n"
            )

        await update.message.reply_text(message)

    except Exception:
        await update.message.reply_text(
            "❌ د کتابونو په لټون کې ستونزه رامنځته شوه. بیا هڅه وکړئ."
        )
