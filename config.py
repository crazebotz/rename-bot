import os

class Config(object):
    # get a token from @BotFather
    TOKEN = os.environ.get("BOT_TOKEN", "")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
   
    
    # your telegram id
    ADMIN = set(str(x) for x in os.environ.get("ADMIN", "").split())
    CHANNEL = int(os.environ.get("CHANNEL", "-1001332181134"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # database uri (mongodb)
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("MYDATABASE", "MYDB")
    STRING = (os.environ.get("STRING", ""))
 
