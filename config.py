#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')

API_ID = os.environ.get("API_ID", "20790743")
API_HASH = os.environ.get("API_HASH", "266b46661c0eb26ee0cb9ef7dfebfe39")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6903924252:AAEOksl2QZDL-9-fpjGsKFW2am5qYRm1ZFQ")
ADMIN = int(os.environ.get("ADMIN", '6474527080'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Sujan_BotZ")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "https://t.me/+EDWt66RD6vo4YzQ1")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://gimojo1891:gimojo1891@cluster0.ufujobd.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://telegra.ph/file/2bb4f8214d21484159fda.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '5123039648'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", "-1001826322671")
