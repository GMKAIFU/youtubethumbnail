import telebot
import re

BOT_TOKEN = '8195052928:AAHlGmxPSUOBvcyKEyY5eDblm7UYPIWHoAY'  # 👈 Replace with your Telegram Bot Token
bot = telebot.TeleBot(BOT_TOKEN)

def extract_video_id(url):
    regex = r"(?:v=|youtu\.be/|embed/|v/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None

def get_thumbnail_url(video_id):
    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "👋 Send a YouTube link and I’ll give you the thumbnail!")

@bot.message_handler(func=lambda m: True)
def send_thumbnail(msg):
    video_id = extract_video_id(msg.text)
    if video_id:
        thumb_url = get_thumbnail_url(video_id)
        bot.send_photo(msg.chat.id, thumb_url, caption="✅ Here’s the thumbnail!")
    else:
        bot.send_message(msg.chat.id, "⚠️ Invalid YouTube link.")

print("🤖 Bot is running...")
bot.infinity_polling()
