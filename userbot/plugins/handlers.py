from pyrogram.errors import BadRequest
from pyrogram import filters
from userbot import UserBot
from userbot.plugins.help import add_command_help
from userbot.helpers.PyroHelpers import GetChatID
import time
import os
from pathlib import Path
import sys
from shutil import copyfile

@UserBot.on_message(filters.me & filters.text & filters.command("sendall","."))
async def send_all(client, message):
    cmd = message.command
    try:
        msg = cmd[1]
        async for d in client.iter_dialogs():
            try:
                await client.send_message(chat_id=d.chat.id, text=msg)
            except:
                continue
    except Exception as error:
        await client.send_message(message.chat['id'],reply_to_message_id=int(message.message_id),text="sendall error : " + str(error))


@UserBot.on_message(filters.me & filters.text & filters.command("getchats","."))
async def getchats(client, message):
    cmd = message.command
    async for d in client.iter_dialogs():
        try:
            await client.send_message(chat_id=message.chat.id, text=f"{d.chat.id} belongs to {d.chat.username}")
        except:
            continue


@UserBot.on_message(filters.me & filters.text & filters.command("load_plugin","."))
async def plugin_add(client, message):
    cmd = message.command
    try:
        if len(cmd) > 1:
            filename = cmd[1]
            downloads_dir = str(UserBot.WORKDIR) + "/userbot/downloads"
            plugins_dir = str(UserBot.WORKDIR) + "/userbot/plugins"
            copyfile(f"{downloads_dir}/{filename}",f"{plugins_dir}/{filename}")
            await client.send_message(message.chat['id'],"restart bot to load plugin command : .restart")
    except Exception as error:
        await client.send_message(message.chat['id'],"loading_plugin error : " + str(error))


@UserBot.on_message(filters.me & filters.text & filters.command("hi","."))
async def hi(client, message):
    await message.edit("""
    🌺✨✨🌺✨🌺🌺🌺
🌺✨✨🌺✨✨🌺✨
🌺🌺🌺🌺✨✨🌺✨
🌺✨✨🌺✨✨🌺✨
🌺✨✨🌺✨🌺🌺🌺
☁️☁️☁️☁️☁️☁️☁️☁️
    """)

@UserBot.on_message(filters.me & filters.text & filters.command("sendgroup","."))
async def send_group(client, message):
    cmd = message.command
    msg = cmd[1]
    groups = ["supergroup","group","channel"]
    async for d in client.iter_dialogs():
        if d.chat.type in groups:
            try:
                await client.send_message(chat_id=d.chat.id, text=msg)
            except Exception as error:
                await message.reply(str(error))
                continue
            # print(d.chat.type)

@UserBot.on_message(filters.me & filters.text & filters.command("get_info","."))
async def get_info(client, message):
    cmd = message.command
    if len(cmd) > 1:
        try:
            info = await client.get_chat(cmd[1])
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=info)
        except BadRequest as error:
            # print(error.args)
            # print(info)
            if info.photo:
                await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="**photo**\n"+str(info.photo))

            if info.description:
                await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="**description**\n"+str(info.description))

            if info.permissions:
                await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="**permissions**\n"+str(info.permissions))

@UserBot.on_message(filters.me & filters.text & filters.command("gdn","."))
async def goodnight(client, message):
    await message.edit("""
        ｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･
╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮
╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮
┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫
┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯
╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯
｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ
        """)
@UserBot.on_message(filters.me & filters.text & filters.command("gdm","."))
async def gdm(client, message):
    await message.edit("""
    ｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･｡♥️｡･ﾟ♡ﾟ･
╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮
╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮
┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃
┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃
╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯
｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･｡♥️｡･ﾟ♡ﾟ･""")


@UserBot.on_message(filters.me & filters.text & filters.command("lol","."))
async def lol(client, message):
    await message.edit("😂🤣😂🤣😂🤣😂🤣")
    time.sleep(0.4)
    await message.edit("🤣😂🤣😂🤣😂🤣😂")
    time.sleep(0.4)
    await message.edit("😂🤣😂🤣😂🤣😂🤣")
    time.sleep(0.4)
    await message.edit("🤣😂🤣😂🤣😂🤣😂")
    await message.edit("""
    ╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ 
╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ 
╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ 
╱┗━━━┛╰━━━╯┗━━━┛╱
    """)

@UserBot.on_message(filters.me & filters.text & filters.command("download","."))
async def download(client, message):
    cmd = message.command
    if len(cmd) > 1:
        try:
            filename = cmd[1]
            # extention = message.reply_to_message
            # print(message.reply_to_message)
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="Downloading...")
            comd = d.message_id
            comdchat = d.chat['id']
            async def progress(current, total):
                pro = f"{current * 100 / total:.1f}%"
                await client.edit_message_text(comdchat,comd,pro)
            await client.download_media(message=message.reply_to_message,file_name=str(UserBot.WORKDIR) + "/userbot/downloads/" + filename, progress=progress)
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
    else:
        try:
            # extention = message.reply_to_message
            # print(message.reply_to_message)
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="Downloading...")
            comd = d.message_id
            comdchat = d.chat['id']
            async def progress(current, total):
                pro = f"{current * 100 / total:.1f}%"
                await client.edit_message_text(comdchat,comd,pro)
            await client.download_media(message=message.reply_to_message,file_name=str(UserBot.WORKDIR) + "/userbot/downloads/", progress=progress)
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
   


         
add_command_help(
    "general",
    [
        [
            ".gdn",
            "show a goodnigth design\nUsage: ``.gdn``",
        ],[
            ".gdm",
            "show a goodMorning design\nUsage: ``.gdm``",
        ],[
            ".sendall",
            "Send message to all chats\nUsage: ``.sendall``",
        ],[
            ".getchats",
            "send chat id of all chats\nUsage: ``.getchats``",
        ],
        [
            ".lol",
            "show some faces\nUsage: ``.lol``",
        ],
        
        [
            ".sendgroup",
            "send message to all groups only\nUsage: ``.sendgroup <message>``",
        ],[
            ".download",
            "Download file in download folder\nUsage: ``.download <reply to file>``",
        ],
        [
            ".get_info",
            "get info about a user or group or channel\nUsage: ``.get_info <userid | usertelegram id | group id | channel id>``",
        ],[
            ".load_plugin",
            "load plugin from download directory to plugin directory\nyou can check files in downloads directory using .ls downloads\nUsage: ``.load_plugin <plugin name in download directory>``",
        ],[
            ".hi",
            "show a HI design\nUsage: ``.gdm``",
        ],
        
        
    ],
)
