from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "25377875"))
    API_HASH = getenv("API_HASH", "cf80e342be48570ca2e4c9d2c7695413")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://Selfmixbot:nehalsingh969797@cluster0.kb5xjos.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "-1002392579812 -1002046689277 -1001938178416 -1001974758661 -1001903984533 -1001943196163 -1001831242679 -1001933661992 -1002154419710 -1002215662728 -1002136558316 -1001951247170").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "ns")
    PASSWORD = getenv("PASSWORD", "ns")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "nehal")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "nehal")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
