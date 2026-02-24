from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = 34526092
        self.API_HASH = "0de81a7870354f026d084985376becb0"

        self.BOT_TOKEN = getenv("8512639516:AAEARNkbtgJQsgWpPpsxC4woZSXrhi8da7E")
        self.MONGO_URL = "mongodb+srv://khargosh:khargosh@cluster0.2fimped.mongodb.net/?appName=Cluster0"

        self.LOGGER_ID = -1002843633996
        self.OWNER_ID = 8319024738

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 600000000)) * 600000000
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 200000000000))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 200000000000))

        self.SESSION1 = getenv("BQIB5IkAv3JeyLExKg5ax49E8WhCYsm4EEvcv5zlY9_JsLq91ZOV64nxCtM94RWiK7H9IkgynPLnT9aQnU22lmlde-tyvXu4KecUWUwRTJfQmF38IYJEN6Y5atudNN-cVhcaQh-L9ADjjnxocMl6AF0q7Stm-wG5vFF1JGRjlgDSOvM1l_4A-LwFiy9lrkULMW2AyoQ6nEwAWx2Z4QzogkcciiAAEP4pkBGMZaEoiz45U2TxfIRauj9bvUMGdtMAU35OlzAwnkkSnaiovS7U6IexzjK9iqTbXIx1ijmXqyZOlKy1NIHXMxHU3S9Ik0BdkQTfurcWc6fZ4nSpDEdb8oefxqpVygAAAAHuQUkQAA", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = "https://t.me/khargosh_updates"
        self.SUPPORT_CHAT = "https://t.me/khargosh_support"

        self.AUTO_END: bool = getenv("AUTO_END", True)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/captors").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = "https://ar-hosting.pages.dev/1770755014036.jpg"
        self.PING_IMG = "https://ar-hosting.pages.dev/1770755014036.jpg"
        self.START_IMG = "https://ar-hosting.pages.dev/1770755014036.jpg"

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
