import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5570243067:AAEI_RnFlFvTlbkSQYc_fA0KHDXl4twOgG8")

    API_ID = int(os.environ.get("API_ID", 23560088))

    API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5410723702").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001666254490")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = "kLgE2EQm"

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @ulruploaderv2bot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://amit:amit@cluster0.fdlnmlh.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "ulruploaderv2bot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001642382009"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "5410723702"))


    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001666254490")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ulruploaderv2bot")
