import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8932326265:AAGxB2Oz3-XWc_PDO-ic5o3vGdJcILpsnuM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("credit", callback_data="credit"),
            InlineKeyboardButton("usage", callback_data="usage")
        ],
        [
            InlineKeyboardButton("referral", callback_data="referral"),
            InlineKeyboardButton("tutorial", callback_data="tutorial")
        ],
        [
            InlineKeyboardButton("support", callback_data="support")
        ]
    ])
    await update.message.reply_text("welcome", reply_markup=keyboard)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "credit":
        await query.edit_message_text("credit: 0")
    elif query.data == "usage":
        await query.edit_message_text("usage: 0 GB")
    elif query.data == "referral":
        await query.edit_message_text("referral link: t.me/Glassnetbot")
    elif query.data == "tutorial":
        await query.edit_message_text("tutorial: download - install - connect")
    elif query.data == "support":
        await query.edit_message_text("support: @YourSupport")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
