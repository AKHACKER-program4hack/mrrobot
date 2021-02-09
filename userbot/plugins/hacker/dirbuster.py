from pyrogram.errors import BadRequest, Forbidden

from pyrogram import filters

from userbot import UserBot
from userbot.helpers.PyroHelpers import GetChatID
from userbot.plugins.help import add_command_help
import time
import requests

@UserBot.on_message(filters.me & filters.text & filters.command("dirb","."))
async def dirbuster(client, message):
    cmd = message.command
    try:
        if len(cmd) > 2:
            url = cmd[1]
            wordlisturl = cmd[2]
            try:
                print("in brute")
                wordlist = requests.get(wordlisturl).content.decode("utf-8").split()
                d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="Attack started...")
                msgid = d.message_id
                chatid = d.chat['id']
                comd = message.message_id
                comdchat = message.chat['id']
                # for i in range(1000):
                #     msg = await client.get_messages(comdchat,comd)
                #     print(msg.text)
                #     time.sleep(5)
                for word in wordlist:
                    msg = await client.get_messages(comdchat,comd)
                    if msg.text == None:
                        await client.send_message(chat_id=chatid, reply_to_message_id=int(msgid), text="Attack stopped...")
                        break
                    else:
                        try:
                            r = requests.get(url+word)
                            print("trying : " + word)
                            if r.status_code == 200:
                                await client.send_message(chat_id=chatid,reply_to_message_id=msgid,text="\nfound : " + url + word)
                        except Exception as error:
                            await message.reply(str(error))
                            continue
            except Exception as error:
                await message.reply(str(error))
    except Exception as error:
        await message.edit("Error : " + str(error))
        
        
add_command_help(
    "hackers",
    [
        [
            ".dirb",
            "perform directory brute force on a website\nyou can use github wordlist url in raw view\nUsage: ``.dirb <website url> <wordlist url>``",
        ],
    ],
)
