from pyrogram import filters
from userbot import UserBot
from userbot.plugins.help import add_command_help
from userbot.helpers.PyroHelpers import GetChatID
import time
import os
from pathlib import Path
import sys
from shutil import copyfile
import magic

@UserBot.on_message(filters.me & filters.text & filters.command("ls","."))
async def list_dir(client, message):
    cmd = message.command
    if len(cmd) > 1:
        try:
            directory_param = cmd[1]
            directory = UserBot.main_directory + "/userbot" + "/" + directory_param# + f"/{directory}"
            files = os.listdir(directory)
            view = "**__List items in "+ directory_param + "__** : \n"
            for f in files:
                if os.path.isdir(directory + "/" + f):
                    view += "\n📂 " + f
                else:
                    view += "\n📄 " + f
            await client.delete_messages(GetChatID(message),message.message_id)
            d = await client.send_message(chat_id=message.chat["id"], text=view)
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
    else:
        try:
            # extention = message.reply_to_message
            # print(message.reply_to_message)
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="invalid directory")
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
   
@UserBot.on_message(filters.me & filters.text & filters.command("del","."))
async def download(client, message):
    cmd = message.command
    if len(cmd) > 1:
        try:
            file_param = cmd[1]
            file_to_del = UserBot.main_directory + "/userbot" + "/" + file_param# + f"/{directory}"
            try:
                status = os.system("rm -rf \"" + file_to_del + "\"")
                d = await client.send_message(chat_id=message.chat["id"], text="deleted\n")
                await client.delete_messages(GetChatID(message),message.message_id)
                time.sleep(3)
                await client.delete_messages(GetChatID(d),d.message_id)
            except Exception as error:
                d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
            
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
    else:
        try:
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="invalid directory")
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
   
@UserBot.on_message(filters.me & filters.text & filters.command("send","."))
async def send_files(client, message):
    cmd = message.command
    async def progress(current, total):
        await message.edit(f"uploaded {current * 100 / total:.1f}%")

    if len(cmd) > 1:
        try:
            file_param = cmd[1]
            if cmd[2]:
                caption_text = cmd[2]
            else: caption_text = None
            file_to_upload = str(UserBot.WORKDIR) + "/userbot" + "/" + file_param# + f"/{directory}"
            try:
                filetype = magic.from_file(file_to_upload)
                if "document" in filetype:
                    await UserBot.send_document(GetChatID(message), file_to_upload, progress=progress,caption=caption_text)
                elif "script" in filetype:
                    await UserBot.send_document(GetChatID(message), file_to_upload, progress=progress,caption=caption_text)
                elif "GIF" in filetype:
                    await UserBot.send_animation(GetChatID(message), file_to_upload, progress=progress,caption=caption_text)
                elif "image" in filetype:
                    await UserBot.send_photo(GetChatID(message), file_to_upload, progress=progress,caption=caption_text)
                elif "Media" in filetype:
                    await UserBot.send_video(GetChatID(message), file_to_upload, progress=progress,caption=caption_text)
                elif "Audio" in filetype:
                    await UserBot.send_audio(GetChatID(message), file_to_upload, progress=progress,caption=caption_text)
                await client.delete_messages(GetChatID(message),message.message_id)
                time.sleep(3)
            except Exception as error:
                d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
            
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
    else:
        try:
            d = await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text="invalid directory")
        except Exception as error:
            await client.send_message(chat_id=message.chat["id"], reply_to_message_id=int(message.message_id), text=str(error))
   

add_command_help(
    "filemanager",
    [
        [
            ".ls",
            "show list of files in a directory\nUsage: ``.ls <directory name>``",
        ],[
            ".del",
            "Delete file or directory\nUsage: ``.del <path>``",
        ],
        [
            ".send",
            "send file from any directory\nUsage: ``.send <path> <caption>``",
        ],
        
        
    ],
)
