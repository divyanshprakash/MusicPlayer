
import os
import re
from youtube_dl import YoutubeDL
ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "https://youtu.be/BxhDqNeTHKM")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", '1250630952')
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", '6239579'))
    CHAT = int(os.environ.get("CHAT", "-1001172836875"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001172836875")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    ARQ_API=os.environ.get("ARQ_API", "DXBOAO-MVWXVU-OIUMQY-ZVTTIH-ARQ")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "NO":
        EDIT_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 10000))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "0a6bb5be3bec0cb8ed7c408a45f02f4c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1938493507:AAH6-PLMIfHDIe0sTF1XkPw_J0IZ-dyFLjM") 
    SESSION = os.environ.get("SESSION_STRING", "BQCGtpP6rvtC0jnZa4YNWEV5DAnfk-uZi1qNyFqBoeLsbapH-G_LJVwCQeu2ouYljGyfZ16vmZD-X-3L3VJ6yeFLEOzIVJHzYXz0IMk2GS3ADFXYykrXTiRGZC_OWovj8j7UyHdLFig22QZMpkX4YyrvOpsSgLvJV5HKrmgFgFNQVPyvYC-bn8nl3XLykuBfXf5wLtFokNQon_WNVKeCD_pyxcF9SWyuN2QR3AgRUL_Mjpnv9UnM4rJjEdKcuoPMeKL5Sv56qiJ7kU0Jmk8ZbTC8iaSM8KF2313Q8BmdPiVN9CE0nCkIaTplmDSl8uJExwexvWqSHqKGE7vdDosd5Y5oYaBlPwA")
    playlist=[]
    msg = {}
