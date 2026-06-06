from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8932326265:AAGxB2Oz3-XWc_PDO-ic5o3vGdJcILpsnuM"

MENU = [
    ["💰 اعتبار من", "⏳ میزان مصرف"],
    ["👥 معرفی به دوستان", "💡 آموزش استفاده"],
    ["🧑‍💻 تماس با پشتیبانی"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    await update.message.reply_text(
        "سلام، خوش آمدید 🌿\n\n"
        "سرویس‌های ما با سرعت بالا، کیفیت پایدار و پشتیبانی "
        "تا آخرین روز اشتراک ارائه می‌شوند.\n\n"
        "برای اطمینان خاطر شما، ضمانت بازگشت وجه نیز داریم.",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💰 اعتبار من":
        await update.message.reply_text("اعتبار شما: ۰ تومان\nبرای شارژ با پشتیبانی تماس بگیرید.")
    elif text == "⏳ میزان مصرف":
        await update.message.reply_text("میزان مصرف: ۰ گیگابایت")
    elif text == "👥 معرفی به دوستان":
        await update.message.reply_text("لینک معرفی شما:\nt.me/YourBot?start=ref_12345")
    elif text == "💡 آموزش استفاده":
        await update.message.reply_text("آموزش اتصال:\n1. فایل را دانلود کنید\n2. نصب کنید\n3. متصل شوید")
    elif text == "🧑‍💻 تماس با پشتیبانی":
        await update.message.reply_text("پشتیبانی: @YourSupport")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
