
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
STREAM=os.environ.get("STREAM_URL", "https://eu10.fastcast4u.com/clubfmuae")
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
    SESSION = os.environ.get("SESSION_STRING", "BQAvVIPjC4GsmJ6oBmvNYRd1ITtF0zBKxxOTVGjABJY2B-htpwK1L5JUu4gnZMgxW1lLYs-CyhnpxNNKTZdYOKsi5i2zMrGCLKCwczHXj_lTFvgub3KZWPhlevcSnEd0Kqdt9rQPUuZvsPEvrxott4SBDtjdF3a8B6nclYwMfy-SO2_ECP3Y6Sy5rbh2Ked7afnk7Zw_zHaolTQq8V6xmmOHNUU9lHcGwMdN6ZulundYLDzhxptUYdwVH7qCqXd4SUM57sybVmx6Kda-yzE3wTSlz6JhdeAx5zfrG6PCN45eQBUrD94DC7AgiqKGkrX8a9oQ5Oky0_98UOIkTuno5m8TYaBlPwA")
    playlist=[]
    msg = {}
