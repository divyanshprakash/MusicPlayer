
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
    SESSION = os.environ.get("SESSION_STRING", "BQAfaVxMy4mKWCxrlCyRobiZFPb1QUeobi9gb5t4vLfsgHCRJLFui2SDi4BHoVQbRC99UDTJc1T6FddKGoi1DSw60hIxXdS3iWk0a54jrWvc7wQ87xr44n1To1ULKb_ejQ_qXVYhNcClqzt3KYaEB601LQgHFPTfiA7aWTOHD74fXkeQnS0k_Nz8h5l2aTAZF83EXp4Y5MuuAHPLeOWc9NYXnGFInL20-fVqwx-1rBAt2F5mrH-0BkEXyDNT7XjVhTLOgHk8p0YMnwn_gSwT0ZiG3flHkI_zBo3Jq3z2MvkLjGwg3ajOc5PFfzYbWqkrlVEzz0QQYIXEjX77AjEldej5YaBlPwA")
    playlist=[]
    msg = {}
