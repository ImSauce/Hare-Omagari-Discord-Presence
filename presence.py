from pypresence import Presence
import time
import datetime
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Discord Client ID (use ur own .env with CLIENT="ur discord application client ID")
CLIENT_ID = os.getenv("CLIENT")
RPC = Presence(CLIENT_ID)

try:
    RPC.connect()
    print("[SUCCESS] Hare Successfully connected to discord 💚")
except Exception as e:
    print(f"[ERROR] Oh no, something went wrong : {e}")
    exit(1)


# Auto Time = 0
# Custom Time = more than 1
custom_auto=1

if custom_auto == 0:
    start_time = int(time.time())
else:
    # Custom start time: May 26, 2025, 10:00 AM UTC
    custom_start = datetime.datetime(2025, 5, 26, 10, 0, 0)
    start_time = int(custom_start.timestamp())



# Hare Data
RPC.update(
    state="Servers hacked",
    details="Programming with Hare",
    start=start_time,
    large_image="hare", # add the asset in ur application in "rich presence > art assets > add image(s)" in the discord developer portal. (image size must be atleast 512x512 minimum)     
    large_text="小鈎ハレ",
    small_image="green",  # do the same thing in the large_image comment.    
    small_text="Verified",
    party_id="hare_party_001",             
    party_size=[59, 400],                     
    # buttons=[
    #     {"label": "ハレの歌声", "url": "https://www.youtube.com/watch?v=q5gur6wbgDQ"},
    # ]
)


try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("\n[DEACTIVATE] deactivating hare presence...")
    RPC.clear()
    RPC.close()
