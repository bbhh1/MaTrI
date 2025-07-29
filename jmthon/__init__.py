
# مشروع ماتركس - نسخة معدلة

import logging
import time
import sys
import os
from dotenv import load_dotenv
import jmthon.core.ubclient
from .config import Var
from .core.client import JmthonClient
from telethon.sessions import StringSession
from .core.session import both_session
from .core.logger import *
from database import jmdB, JmdB

load_dotenv()  # تحميل متغيرات البيئة من ملف .env

version = "1.0.0"
start_time = time.time()

bot_token = os.getenv("BOT_TOKEN")  # قراءة التوكن من ملف .env

jmubot = jmthon_bot = JmthonClient(
    session=StringSession(str(Var.SESSION)),
    app_version=version,
    device_model="Jmthon",
)

tgbot = asst = JmthonClient("Tgbot", bot_token=bot_token)

del bot_token

HNDLR = jmdB.get_key("HNDLR") or "."
SUDO_HNDLR = jmdB.get_key("SUDO_HNDLR") or HNDLR
