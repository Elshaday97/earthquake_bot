from telegram import Update
from telegram.ext import ContextTypes
from services.api import fetch_earthquake_data
from bot.poster import post_to_telegram


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Use /latest to see earthquakes reported in Ethiopia in the past 24 hours."
    )


async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    data = fetch_earthquake_data()
    features = data.get("features", [])

    if features:
        for feature in features:
            await post_to_telegram(chat_id, feature)
    else:
        await update.message.reply_text(
            "No earthquakes in Ethiopia were reported in the past 24 hours."
        )


def error_handler(update, context):
    print(f"Error occurred: {context.error}")
