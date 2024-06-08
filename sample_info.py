from info import DATABASE_URI

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 26626715
API_HASH = '967f1c73aa77a29009bc364edd30b525'
BOT_TOKEN = '7400707493:AAGbj53YNBBzYmVw_oqZUS1j3kkBPWyA_Os'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_NAME = 'DQ FILTER BOT'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

#temp dict for storing the db uri which will be used for storing user, chat and file infos
tempDict = {'indexDB': DATABASE_URI}
