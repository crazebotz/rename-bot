import os

class Config(object):
    # get a token from @BotFather
    TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    # Get these values from my.telegram.org
    
 
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DB_URL = os.environ.get("DATABASE_URL", "")
    DB_NAME = os.environ.get("MYDATABASE", "")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER")
