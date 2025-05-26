#import pypresence and dotenv first using pip install in the terminal
from pypresence import Presence
import time
import datetime
import os
from dotenv import find_dotenv, load_dotenv

#my .env file is private so u cant use it, u must create your own
# Make sure the inside of ur .env file includes: CLIENT="your Discord application client ID"
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


# Retrieve the Discord Client ID from the .env
CLIENT_ID = os.getenv("CLIENT")
RPC = Presence(CLIENT_ID)

try:
    RPC.connect()
    print("[SUCCESS] Hare Successfully connected to discord 💚")
except Exception as e:
    print(f"[ERROR] Oh no, something went wrong : {e}")
    exit(1)

#switch between custom time or automatic real time
use_custom_time = True

if use_custom_time == True:
    # Custom start time: May 26, 2025, 10:00 AM UTC
    custom_start = datetime.datetime(2025, 5, 26, 10, 0, 0)
    start_time = int(custom_start.timestamp())
else: #if false, it will use automatic time
    start_time = int(time.time())



# Hare Data
RPC.update(
    state="Servers hacked",
    details="Programming with Hare",
    start=start_time,
    large_image="hare_image", # use your own images and add them in ur application in "rich presence > art assets > add image(s)" in the discord developer portal. (image size must be atleast 512x512 minimum)     
    large_text="小鈎ハレ",
    small_image="green_verfied_image",  # do the same thing in the large_image comment.    
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
