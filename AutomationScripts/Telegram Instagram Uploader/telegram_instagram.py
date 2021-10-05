# --- imports --- #
import os
import logging
from instagrapi import Client
from telethon import TelegramClient
from telethon.events import NewMessage

# --- Required Vars --- #
INSTAGRAM_USERNAME = "" or input("Enter Your Instagr Username : ")
INSTAGRAM_PASSWORD = "" or input("Enter your Instagram Password :")

API_ID = 6  # Telegram API ID
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"  # Telegram API HASH
TG_BOT_TOKEN = "" or input("Enter Telegram Bot Token")  # Telegram BOT_TOKEN
TG_CHATIDS = [] or [
    int(chat) for chat in input("Enter Chat Ids : ")
]  # List of Telegram Chat Ids

# ------ Main ------ #
logging.basicConfig(level=logging.INFO)  # set logging level

# Create Instagram Client
settings = "settings.json" if os.path.exists("settings.json") else None
InstaClient = Client()

# So That, it doesnt create session again and again
if settings:
    InstaClient.load_settings(settings)
    InstaClient.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
else:
    InstaClient.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    InstaClient.dump_settings("settings.json")

# Creatimg Telegram Client
Client = TelegramClient("Tele-Insta-BOT", api_id=API_ID, api_hash=API_HASH)
Client = Client.start(bot_token=TG_BOT_TOKEN)


# Function/Haner to get Telegram Event Update with Video And Chat Filter.
@Client.on(NewMessage(chats=TG_CHATIDS, func=lambda e: e.video))
async def upload_to_insta(event):
    msg = await event.reply("Downloading Video...")
    caption = event.message.message or "#Auto"
    file = await event.download_media()
    msg = await msg.edit("Uploading Now...")
    try:
        video = InstaClient.clip_upload(file, caption=caption)
    except Exception as ER:
        print(ER)
        os.remove(file)
        return await msg.edit(str(ER))
    m = "Uploaded to Instagram\n"
    m += f"https://instagram.com/p/{video.code}"
    await msg.edit(m)
    os.remove(file)  # remove file adter use..


with Client:
    Client.run_until_disconnected()
    # Start And Loop Telegram Client
