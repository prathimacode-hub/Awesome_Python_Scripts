 # --- imports --- #
import os
import logging
from instagrapi import Client
from telethon import TelegramClient
from telethon.events import NewMessage

# --- Required Vars --- #
INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""

API_ID = 6  # Telegram API ID
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"  # Telegram API HASH
TG_BOT_TOKEN = ""  # Telegram BOT_TOKEN
TG_CHATIDS = []  # List of Telegram Chat Ids

# ------ Main ------ #
logging.basicConfig(level=logging.INFO)
settings = "settings.json" if os.path.exists("settings.json") else None
InstaClient = Client()

# So That, it doesnt create session again and again
if settings:
    InstaClient.load_settings(settings)
    InstaClient.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
else:
    InstaClient.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
    InstaClient.dump_settings("settings.json")

Client = TelegramClient("Tele-Insta-BOT", api_id=API_ID, api_hash=API_HASH)
Client = Client.start(bot_token=TG_BOT_TOKEN)


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
    os.remove(file)


with Client:
    Client.run_until_disconnected()

