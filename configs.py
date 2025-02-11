from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28713982"))
    API_HASH = getenv("API_HASH", "237e15f7c006b10b4fa7c46fee7a5377")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO", "7195990500").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
