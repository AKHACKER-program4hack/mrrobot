import asyncio
from datetime import datetime
from platform import python_version

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import __version__

from userbot import UserBot, START_TIME
from userbot.helpers.constants import First
from userbot.plugins.help import add_command_help


@UserBot.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, message: Message):
    txt = (
        f"**{UserBot.__class__.__name__}** ```RUNNING```\n"
        f"-> Current Uptime: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"-> Python: `{python_version()}`\n"
        f"-> Pyrogram: `{__version__}`"
    )
    await message.edit(txt)


@UserBot.on_message(filters.command("repo", ".") & filters.me)
async def repo(_, message: Message):
    await message.edit(First.REPO)


@UserBot.on_message(filters.command("creator", ".") & filters.me)
async def creator(_, message: Message):
    await message.edit(First.CREATOR)


@UserBot.on_message(filters.command(["uptime", "up"], ".") & filters.me)
async def uptime(_, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await message.edit(f"Current Uptime\n" f"```{str(current_uptime).split('.')[0]}```")


@UserBot.on_message(filters.command("id", ".") & filters.me)
async def get_id(_, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID**: `{rep.audio.file_id}`"
            file_id += f"**File Ref**: `{rep.audio.file_ref}`"
            file_id += "**File Type**: `audio`"

        elif rep.document:
            file_id = f"**File ID**: `{rep.document.file_id}`"
            file_id += f"**File Ref**: `{rep.document.file_ref}`"
            file_id += f"**File Type**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`"
            file_id += f"**File Ref**: `{rep.photo.file_ref}`"
            file_id += "**File Type**: `photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set**: `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker**: `False`\n"
            else:
                file_id += "**Sticker Set**: __None__\n"
                file_id += "**Sticker Emoji**: __None__"

        elif rep.video:
            file_id = f"**File ID**: `{rep.video.file_id}`\n"
            file_id += f"**File Ref**: `{rep.video.file_ref}`\n"
            file_id += "**File Type**: `video`"

        elif rep.animation:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += f"**File Ref**: `{rep.animation.file_ref}`\n"
            file_id += "**File Type**: `GIF`"

        elif rep.voice:
            file_id = f"**File ID**: `{rep.voice.file_id}`\n"
            file_id += f"**File Ref**: `{rep.voice.file_ref}`\n"
            file_id += "**File Type**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += f"**File Ref**: `{rep.animation.file_ref}`\n"
            file_id += "**File Type**: `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.venue.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address**:\n"
            file_id += f"**title**: `{rep.venue.title}`\n"
            file_id += f"**detailed**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.message_id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.message_id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**Chat ID**: `{message.chat.id}`")


@UserBot.on_message(filters.command("restart", ".") & filters.me)
async def restart(_, message: Message):
    await message.edit(f"Restarting {UserBot.__class__.__name__}.")
    await UserBot.send_message(
        "me", f"#userbot_restart, {message.chat.id}, {message.message_id}"
    )

    if "p" in message.text and "g" in message.text:
        asyncio.get_event_loop().create_task(UserBot.restart(git_update=True, pip=True))
    elif "p" in message.text:
        asyncio.get_event_loop().create_task(UserBot.restart(pip=True))
    elif "g" in message.text:
        asyncio.get_event_loop().create_task(UserBot.restart(git_update=True))
    else:
        asyncio.get_event_loop().create_task(UserBot.restart())


# Command help section
add_command_help(
    "start",
    [
        [".alive", "Check if the bot is alive or not."],
        [".repo", "Display the repo of this userbot."],
        [".creator", "Show the creator of this userbot."],
        [".id", "Send id of what you replied to."],
        [".up `or` .uptime", "Check bot's current uptime."],
    ],
)

add_command_help(
    "restart",
    [
        [".restart", "You are retarded if you do not know what this does."],
        [".restart g", "Pull latest changes from git repo and restarts."],
        [".restart p", "Installs pip requirements restarts."],
        [
            ".restart gp",
            "Pull latest changes from git repo, install pip requirements and restarts.",
        ],
    ],
)
