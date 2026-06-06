import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8932326265:AAGxB2Oz3-XWc_PDO-ic5o3vGdJcILpsnuM"
ADMIN_ID = 8476379154

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
        ],
        [
            InlineKeyboardButton("🛒 خرید سرویس", url="https://t.me/mobinzam")
        ]
    ])
    await update.message.reply_text("سلام خوش آمدید 🌿", reply_markup=keyboard)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    back = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 بازگشت", callback_data="back")]])
    if query.data == "back":
        await start_from_callback(query)
    elif query.data == "credit":
        await query.edit_message_text("اعتبار شما: 0 تومان", reply_markup=back)
    elif query.data == "usage":
        await query.edit_message_text("مصرف: 0 GB", reply_markup=back)
    elif query.data == "referral":
        await query.edit_message_text("لینک: t.me/Glassnetbot", reply_markup=back)
    elif query.data == "tutorial":
        await query.edit_message_text("آموزش: دانلود - نص
