import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    print(f"Got: {message.text} from {message.from_user.first_name}")
    bot.reply_to(message, "Working! البوت يخدم توا ✅")

print("Bot is running... go to Telegram now")
bot.infinity_polling(skip_pending=True)