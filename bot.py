import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, ChatMemberStatus
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8932326265:AAGxB2Oz3-XWc_PDO-ic5o3vGdJcILpsnuM"
CHANNEL = "@vpnfasttttte"

async def check_member(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_my_commands([BotCommand("start","start"),BotCommand("new","new service"),BotCommand("renew","renew"),BotCommand("status","status")])
    user_id = update.message.from_user.id
    is_member = await check_member(context.bot, user_id)
    if not is_member:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/vpnfasttttte")],
            [InlineKeyboardButton("عضو شدم", callback_data="check_join")]
        ])
        await update.message.reply_text("برای استفاده از ربات ابتدا در کانال ما عضو شوید.", reply_markup=keyboard)
        return
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("credit", callback_data="credit"),InlineKeyboardButton("usage", callback_data="usage")],
        [InlineKeyboardButton("referral", callback_data="referral"),InlineKeyboardButton("tutorial", callback_data="tutorial")],
        [InlineKeyboardButton("support", callback_data="support")]
    ])
    await update.message.reply_text("welcome", reply_markup=keyboard)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "check_join":
        is_member = await check_member(context.bot, query.from_user.id)
        if not is_member:
            await query.edit_message_text("هنوز عضو نشدید! لطفا ابتدا عضو کانال شوید.")
            return
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("credit", callback_data="credit"),InlineKeyboardButton("usage", callback_data="usage")],
            [InlineKeyboardButton("referral", callback_data="referral"),InlineKeyboardButton("tutorial", callback_data="tutorial")],
            [InlineKeyboardButton("support", callback_data="support")]
        ])
        await query.edit_message_text("welcome", reply_markup=keyboard)
    elif query.data == "credit":
        await query.edit_message_text("credit: 0")
    elif query.data == "usage":
        await query.edit_message_text("usage: 0 GB")
    elif query.data == "referral":
        await query.edit_message_text("referral link: t.me/Glassnetbot")
    elif query.data == "tutorial":
        await query.edit_message_text("tutorial: download - install - connect")
    elif query.data == "support":
        await query.edit_message_text("support: @YourSupport")

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("new service: @mobinzam")

async def renew(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("renew: @mobinzam")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("status: 0 GB")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler("new", new))
    app.add_handler(CommandHandler("renew", renew))
    app.add_handler(CommandHandler("status", status))
    app.run_polling()
