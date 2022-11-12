import os
import json

from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    ALLOW_HOSTS = json.loads(os.environ.get("ALLOW_HOSTS", "['duthaho.github.io','localhost']"))
    SECRET_KEY = os.environ.get("SECRET_KEY", "Super@s3cret")
    TALK_API = json.loads(os.environ.get("TALK_API", "[]"))
    BOT_NAME = json.loads(os.environ.get("BOT_NAME", "[]"))
