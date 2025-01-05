from telegram.ext import Application, CommandHandler
from bot.handlers import start, latest, error_handler
from config import TELEGRAM_TOKEN


def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("latest", latest))
    application.add_error_handler(error_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
