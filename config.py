import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6544161566:AAGRs0j26zsEecrrzCGzth77tdJ6IF7p8hE")
    
    API_ID = int(os.environ.get("API_ID","22299340"))
    
    API_HASH = os.environ.get("API_HASH","09b09f3e2ff1306da4a19888f614d937")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5380609667"))

    SESSION_NAME = "jidovi4576"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://jidovi4576:B6HywpSzpSqZZ3W@clusterbot2.ezfn734.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
