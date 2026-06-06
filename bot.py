import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8932326265:AAGxB2Oz3-XWc_PDO-ic5o3vGdJcILpsnuM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💰 اعتبار من", callback_data="credit"),
            InlineKeyboardButton("⏳ میزان مصرف", callback_data="usage")

        ],
        [
            InlineKeyboardButton("👥 معرفی به دوستان", callback_data="referral"),
            InlineKeyboardButton("💡 آموزش", callback_data="tutorial")

        ],
        [
            InlineKeyboardButton("🧑 پشتیبانی", callback_data="support")
        ]
    ])
    await update.message.reply_text("سلام خوش آمدید 🌿", reply_markup=keyboard)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "credit":
        await query.edit_message_text("اعتبار شما: 0 تومان")
    elif query.data == "usage":
        await query.edit_message_text("مصرف: 0 GB")
    elif query.data == "referral":
        await query.edit_message_text("لینک: t.me/Glassnetbot")
    elif query.data == "tutorial":
        await query.edit_message_text("آموزش: دانلود - نصب - اتصال")
    elif query.data == "support":
        await query.edit_message_text("پشتیبانی: @mobinzam")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
