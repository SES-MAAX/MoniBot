import os
from dotenv import load_dotenv
import telebot
from scraper import *
from telebot import types


load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
r = request()
markup = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    input_field_placeholder="📊 یکی از گزینه‌ها را انتخاب کنید..."
)

btn1 = types.KeyboardButton(text="💵 دلار")
btn2 = types.KeyboardButton(text="🟡 طلای 24 عیار")
btn3 = types.KeyboardButton(text="🪙 طلای 18 عیار")
btn4 = types.KeyboardButton(text="🥈 نقره 999")
btn5 = types.KeyboardButton(text="👑 سکه امامی")
btn6 = types.KeyboardButton(text="💰 سکه گرمی")
btn7 = types.KeyboardButton(text="💲 تتر")

markup.row(btn1, btn2)
markup.row(btn3, btn4)
markup.row(btn5, btn6)
markup.row(btn7)


@bot.message_handler(commands=["start", "restart"])
def bot_start(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name

    text = f"""🤖 *MoniBot*

سلام *{user_name}*، خوش اومدی! 👋

📈 قیمت‌های بازار ایران رو سریع و ساده دریافت کن.

یکی از دکمه‌های پایین رو انتخاب کن تا قیمت موردنظرت نمایش داده بشه. ⚡

━━━━━━━━━━━━━━━━
💵 ارز | 🟡 طلا | 🥈 نقره
👑 سکه | 💲 تتر
━━━━━━━━━━━━━━━━

✨ نسخه Beta
"""

    bot.send_message(
        chat_id,
        text,
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(commands=["help"])
def bot_help(message):
    text = """🆘 *راهنمای MoniBot*

به بخش راهنمای **MoniBot** خوش اومدی.

از دکمه‌های پایین می‌تونی قیمت‌های لحظه‌ای بازار رو دریافت کنی. 📊

*⌨️ دستورات ربات*

`/start` — نمایش پیام خوش‌آمدگویی و کیبورد ربات.
`/restart` — راه‌اندازی مجدد منوی اصلی.
`/help` — نمایش همین راهنما.

*📌 دکمه‌های موجود*

💵 دلار
🟡 طلای 24 عیار
🪙 طلای 18 عیار
🥈 نقره 999
👑 سکه امامی
💰 سکه گرمی
💲 تتر

━━━━━━━━━━━━━━━━

✨ کافیست یکی از دکمه‌ها را انتخاب کنی تا قیمت آن نمایش داده شود.
"""

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.message_handler(content_types=["text"])
def show_price(message):

    if message.text == "💵 دلار":
        price = dollar_price(r)
        bot.reply_to(message, f"💵 *قیمت لحظه‌ای دلار*\n\n`{price}` ریال", parse_mode="Markdown")

    elif message.text == "🟡 طلای 24 عیار":
        price = gold24(r)
        bot.reply_to(message, f"🟡 *طلای 24 عیار*\n\n`{price}` ریال", parse_mode="Markdown")

    elif message.text == "🪙 طلای 18 عیار":
        price = gold18(r)
        bot.reply_to(message, f"🪙 *طلای 18 عیار*\n\n`{price}` ریال", parse_mode="Markdown")

    elif message.text == "🥈 نقره 999":
        price = silver_999(r)
        bot.reply_to(message, f"🥈 *هر گرم نقره 999*\n\n`{price}` ریال", parse_mode="Markdown")

    elif message.text == "👑 سکه امامی":
        price = sekee_emami(r)
        bot.reply_to(message, f"👑 *سکه امامی*\n\n`{price}` ریال", parse_mode="Markdown")

    elif message.text == "💰 سکه گرمی":
        price = geram_sekee(r)
        bot.reply_to(message, f"💰 *سکه گرمی*\n\n`{price}` ریال", parse_mode="Markdown")

    elif message.text == "💲 تتر":
        price = tether(r)
        bot.reply_to(message, f"💲 *تتر*\n\n`{price}` ریال", parse_mode="Markdown")


bot.infinity_polling(skip_pending=True)