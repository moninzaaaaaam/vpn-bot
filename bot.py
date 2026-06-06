import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8932326265:AAGxB2Oz3-XWc_PDO-ic5o3vGdJcILpsnuM"
CHANNEL = "@glassnett"

async def check_member(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status not in ["left", "kicked"]
    except:
        return False

async def show_main_menu(msg):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 خرید سرویس جدید", callback_data="new")],
        [InlineKeyboardButton("📦 سرویس های من", callback_data="myservices")],
        [InlineKeyboardButton("📚 آموزش ها", callback_data="tutorial")]
    ])
    await msg.reply_text("خوش اومدی! چی میخوای؟", reply_markup=keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.set_my_commands([BotCommand("start","start")])
    is_member = await check_member(context.bot, update.message.from_user.id)
    if not is_member:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("عضویت در کانال", url="https://t.me/glassnett")],
            [InlineKeyboardButton("جوجو بلایی شدم", callback_data="check_join")]
        ])
        await update.message.reply_text("جوجو بلا تو چنل که نیستی 😒", reply_markup=keyboard)
        return
    await show_main_menu(update.message)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "check_join":
        is_member = await check_member(context.bot, query.from_user.id)
        if not is_member:
            await query.edit_message_text("هنوز جوجو بلا نشدی! برو عضو شو 😤")
            return
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🛒 خرید سرویس جدید", callback_data="new")],
            [InlineKeyboardButton("📦 سرویس های من", callback_data="myservices")],
            [InlineKeyboardButton("📚 آموزش ها", callback_data="tutorial")]
        ])
        await query.edit_message_text("خوش اومدی! چی میخوای؟", reply_markup=keyboard)
    elif query.data == "new":
        await query.edit_message_text("برای خرید سرویس با پشتیبانی تماس بگیرید: @mobinzam")
    elif query.data == "myservices":
        await query.edit_message_text("سرویس فعال: ندارید")
    elif query.data == "tutorial":
        await query.edit_message_text("آموزش: download - install - connect")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()
