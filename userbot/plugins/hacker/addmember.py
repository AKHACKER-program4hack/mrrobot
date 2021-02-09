import time
from pyrogram import filters
from userbot import UserBot
from userbot.helpers.PyroHelpers import GetChatID
from userbot.plugins.help import add_command_help

@UserBot.on_message(filters.me & filters.text & filters.command("add_members","."))
async def add_m(client, message):
    cmd = message.command
    try:
        fromgroup = cmd[1]
        togroup = cmd[2]
        # cont = 0
        # async for member in client.iter_chat_members(fromgroup):
        #     print(cont)
        #     cont += 1
        if len(fromgroup) > 0 and len(togroup) > 0:
            failed = 0
            added = 0
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="adding members\nadded : " + str(added))
            # print(d)
            msgid = d.message_id
            chatid = d.chat['id']
            comd = message.message_id
            comdchat = message.chat['id']
            # print(cmd)
            async for member in client.iter_chat_members(fromgroup):
                msg = await client.get_messages(comdchat,comd)
                try:
                    if msg.text == None:
                        await d.reply("message is deleted member adding is stopped")
                        break
                    else:
                        # checkbot = # await client.get_users(int(member.user.id))
                        if member.user.is_bot == False:
                            status = await client.add_chat_members(togroup, int(member.user.id))
                            # print(status)
                            if status:
                                await client.edit_message_text(chatid,msgid,"adding members\nadded : " + str(added) + "\nfailed : " + str(failed))
                                added += 1
                            else:
                                await client.edit_message_text(chatid,msgid,"adding members\nadded : " + str(added) + "\nfailed : " + str(failed))
                                failed += 1
                except Exception as error:
                    if "CHAT_ADMIN_REQUIRED" in str(error):
                        await client.send_message(chat_id=GetChatID(message), reply_to_message_id=int(message.message_id), text="CHAT_ADMIN_REQUIRED")
                        failed += 1
                    elif "BROADCAST_FORBIDDEN"in str(error):
                        # await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="BROADCAST_FORBIDDEN")
                        failed += 1
                    elif "CHANNEL_PUBLIC_GROUP_NA"in str(error):
                        # await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="CHANNEL_PUBLIC_GROUP_NA")
                        failed += 1
                    elif "CHAT_ADMIN_INVITE_REQUIRED"in str(error):
                        # await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="CHAT_ADMIN_INVITE_REQUIRED")
                        failed += 1
                    elif "CHAT_FORBIDDEN"in str(error):
                        # await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="CHAT_FORBIDDEN")
                        failed += 1
                    elif "USER_NOT_MUTUAL_CONTACT"in str(error):
                        # await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="USER_NOT_MUTUAL_CONTACT")
                        failed += 1
                    continue
            await client.send_message(chat_id=GetChatID(message), reply_to_message_id=int(message.message_id), text="Finished adding members")
        else:
            await client.send_message(chat_id=GetChatID(message), reply_to_message_id=int(message.message_id), text="Invalid arguments")
    except Exception as error:
        await client.send_message(chat_id=GetChatID(message), reply_to_message_id=int(message.message_id), text="Invalid arguments")
        
add_command_help(
    "hackers",
    [
        [
            ".add_members",
            "ADD MEMBERS from one group to other group \nUsage: ``.add_members <from group username> <to group username>``",
        ],
    ],
)
