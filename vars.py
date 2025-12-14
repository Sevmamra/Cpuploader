#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26797881"))
API_HASH = environ.get("API_HASH", "9699262c708c2e45ba18bfce925ed5ed")
BOT_TOKEN = environ.get("BOT_TOKEN", "8568444176:AAG_csQuqfGH6jSb_ctTEei6lfpLu3voV48")
OWNER = int(environ.get("OWNER", "6567162029"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '5389632871,7556190845,6854842283').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

