import telebot

TOKEN = "এখানে_তোমার_BOT_TOKEN_দাও"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🇧🇩 স্বাগতম BD COIN-এ!\n\n"
        "💰 এখানে কয়েন সংগ্রহ করতে পারবে।\n"
        "🏙️ বাংলাদেশের ৬৪ জেলা নিয়ে আমাদের যাত্রা শুরু!\n\n"
        "👇 মেনু থেকে শুরু করো।"
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "BD COIN বট চালু আছে।")

bot.infinity_polling()Here is the token for bot BDCOIN @BD_COIN_64_BOT:

9072304338:AAGKXhq0Dbnp4o6feWuHWwHmCfxO4I0fr6s

⚠️ WARNING: Anyone can use this token to control your bot. Your account will be held responsible if the bot violates the Telegram Terms of Service.
