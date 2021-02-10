# MR.ROBOT Session creator By AK HACKER
# Owner AKHACKER
# |  \/  |  _ \  |  _ \ / _ \| __ ) / _ \_   _|
# | |\/| | |_) | | |_) | | | |  _ \| | | || |  
# | |  | |  _ < _|  _ <| |_| | |_) | |_| || |  
# |_|  |_|_| \_(_)_| \_\\___/|____/ \___/ |_|  
    

import os


os.system('pip install --upgrade pip')
os.system('pip install Pyrogram==1.1.13')

from pyrogram import Client

robot = """
    |  \/  |  _ \  |  _ \ / _ \| __ ) / _ \_   _|
    | |\/| | |_) | | |_) | | | |  _ \| | | || |  
    | |  | |  _ < _|  _ <| |_| | |_) | |_| || |  
    |_|  |_|_| \_(_)_| \_\\___/|____/ \___/ |_|  
                                            
"""
print(robot)
print("""String Generator. ==> mrrobot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly."""
      )
print("")

APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with Client(":memory:", APP_ID, API_HASH) as c:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    session = c.export_session_string()
    print(session)
    print("")
    print("")
    print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
    ak = c.send_message("me", f"`{session}`")
    ak.reply("The above is the `STRING_SESSION`.")

