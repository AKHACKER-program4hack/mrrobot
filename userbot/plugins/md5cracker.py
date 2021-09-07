from pyrogram import filters
import hashlib
import requests
from userbot import UserBot
from userbot.plugins.help import add_command_help

@UserBot.on_message(filters.me & filters.text & filters.command("md5crack","."))
async def cracker(client, message):
    cmd = message.command
    tries = 0
    totaltries = 0
    hashtocrack = cmd[1]
    try:
        wordlistpath = cmd[2]
    except Exception as error:
        if "list index out of range" in str(error):
            # For local development :
            # wordlistpath = str(Client.WORKDIR) + "/plugins/wordlist/commonpasswordlist.txt"
            # For Production level orignal
            wordlistpath = str(Userbot.WORKDIR) + "/userbot/plugins/wordlist/commonpasswordlist.txt"
        else:
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="Error : " + str(error))
    d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="Cracking started...")
    # await d.edit_text("changes")
    try:
        if (wordlistpath[:7] == "http://") or (wordlistpath[:8] == "https://"):
            wordlist = requests.get(wordlistpath).content.decode("utf-8").split()
        else:
            try:
                with open(wordlistpath,"r") as f:
                    wordlist = f.read().splitlines()
            except Exception as error:
                await d.edit_text("Error : " + str(error))
        countword = len(wordlist)
        try:
            for password in wordlist:
                # print("in for looop")
                # print("tried : " + str(totaltries))
                hashofpassword = hashlib.md5(password.encode("UTF-8")).hexdigest()
                if hashtocrack == hashofpassword:
                    await d.edit_text("cracked : " + str(password))
                    break
                elif password == wordlist[-1]:
                    await d.edit_text("End OF file NO password cracked")
                else:
                    if tries == 50:
                        try:
                            await d.edit_text("Tried : " + str(totaltries) + "/" + str(countword))
                            timewaitrequire = False
                            tries = 0
                        except Exception as error:
                            if timewaitrequire:
                                continue
                            if 'A wait of 1665 seconds is required (caused by "messages.EditMessage")' in str(error):
                                q = await client.send_message(chat_id=d.chat["id"], reply_to_message_id=int(d.message_id), text="Wait regiure to edit message due to large number of editing in message...")
                                timewaitrequire = True
                                continue
                tries += 1
                totaltries += 1
        except Exception as error:
            await d.edit_text("Error : " + str(error))
    except Exception as error:
        if "'utf-8' codec can't decode byte" in str(error):
            await d.text("Error : The wordlist contain some non-ascii character Use correct wordlist")
        elif "The message id is invalid" in str(error):
            e = await client.send_message(chat_id=d.chat["id"], reply_to_message_id=int(d.message_id), text="Cracking stopped...")

        else:
            await d.edit_text("Error : " + str(error))
    
@UserBot.on_message(filters.me & filters.text & filters.command("md5hash","."))
async def hasher(client, message):
    cmd = message.command
    word = cmd[1]
    try:
        wordhash = hashlib.md5(word.encode("utf-8")).hexdigest()
        d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="hash of " + str(word) + " : " + str(wordhash))
    except Exception as error:
        d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="Error : " + str(error))
        
        
add_command_help(
    "hackers",
    [
        [
            ".md5crack",
            "Brute force md5 hash\nUsage: ``.md5crack <md5hash> <wordlist url/path of wordlist if present in download folder>``",
        ],
        [
            ".md5hash",
            "Make md5 hash of a word\nUsage: ``.md5hash password``",
        ],
    ],
)
