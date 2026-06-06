import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, filters, ContextTypes

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
            InlineKeyboardButton("💡 آموزش استفاده", callback_data="tutorial")
        ],
        [
            InlineKeyboardButton("🧑‍💻 تماس با پشتیبانی", callback_data="support")
        ]
    ])
    await update.message.reply_text(
        "سلام، خوش آمدید 🌿\n\nسرویس‌های ما با سرعت بالا ارائه می‌شوند.\n\nضمانت بازگشت وجه داریم.",
        reply_markup=keyboard
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "credit":
        await query.edit_message_text("💰 اعتبار شما: ۰ توم
