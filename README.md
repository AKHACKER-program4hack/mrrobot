# MR.ROBOT Userbot
![Python Version](https://img.shields.io/badge/Python-v3.9-blue)
[![Join Group](https://img.shields.io/badge/Telegram-Join%20Group-informational)](https://t.me/program4hack)
[![Contributors](https://img.shields.io/github/contributors/AKHACKER-program4hack/mrrobot)](https://github.com/AKHACKER-program4hack/mrrobot/graphs/contributors)
![Last Commit](https://img.shields.io/github/last-commit/AKHACKER-program4hack/mrrobot/main)
![Issues](https://img.shields.io/github/issues/AKHACKER-program4hack/mrrobot)
![Pull Requests](https://img.shields.io/github/issues-pr/AKHACKER-program4hack/mrrobot)

<img src="https://telegra.ph/file/0549cdcecfadeab0dfd40.jpg" width="160" align="right">

> A Telegram Userbot based on [Pyrogram](https://github.com/pyrogram/pyrogram)

This repository contains the source code of a Telegram Userbot and the instructions for running a
copy yourself. Beside its main purpose, the bot is featuring [**Pyrogram Asyncio**](https:////github.com/pyrogram/pyrogram/issues/181) and
[**Smart Plugins**](https://docs.pyrogram.org/topics/smart-plugins); feel free to explore the source code to
learn more about these topics.

I assume you will read this whole README.md file before continuing.

> Development in progress.

## Requirements
You're gonna need to get the following programs and services either installed on your server
or signed up for. You must do all. It is a cardinal sin if you don't.

* `virtualenv` installed so that the packages don't interfere with other system packages.

## Installing

<!-- <details>
  <summary> Video Tutorial </summary>

```
Official YouTube Channel Of MR.Robot Owner.
Click on the link below to get tutorial on 
How To Deploy MR.Robot.
```
<a href="https://youtu.be/ifkGhxhlV6Q"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/ifkGhxhlV6Q"><img src="https://img.shields.io/youtube/views/ifkGhxhlV6Q?style=social"></a>

</details> -->

#### Quick Deploy on Heroku using the button down below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AKHACKER-program4hack/mrrobot)

#### Quick Deploy on Railway using the button down below:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FAKHACKER-program4hack%2Fmrrobot&envs=API_ID%2CAPI_HASH%2CUSERBOT_SESSION&API_IDDesc=Get+from+https%3A%2F%2Fmy.telegram.org%2Fapps&API_HASHDesc=Get+from+https%3A%2F%2Fmy.telegram.org%2Fapps&USERBOT_SESSIONDesc=Get+it+from+https%3A%2F%2Freplit.com%2F%40program4hack%2Fmrrobotsessioncreator%23main.py&referralCode=w6Llh-)


*To Get USERBOT_SESSION CLICK Blow Button* :

[![Run on Repl.it](https://repl.it/badge/github/@program4hack/mrrobotsessioncreator#main.py)](https://repl.it/@program4hack/mrrobotsessioncreator#main.py)

*USE Termux To Get USERBOT_SESSION* :

```
pkg install python && pkg install wget && python -m pip install Pyrogram==1.1.13 && wget https://raw.githubusercontent.com/AKHACKER-program4hack/mrrobot/main/sessioncreater.py && python sessioncreater.py
```

*The way I deploy*
```bash
git clone https://github.com/AKHACKER-program4hack/mrrobot.git
cd userbot
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 sessioncreater.py
python3 -m userbot.
```



## Developing
To add extra modules to the bot, simply add the code into [userbot/plugins](userbot/plugins).I have made to functions for it first is ```.download``` which download media you can see in general in help menu and other is ```.load_plugin``` which load_plugin from download directory to plugin directory
.Each file
that is added to the plugins directory should have the following code at a minimum.
```python
from pyrogram import filters

from userbot import UserBot

@UserBot.on_message(filters.command('sample', ['.']))
async def module_name(client, message):
    await message.edit(
        "This is a sample module"
    )
```

This example is only for Pyrogram on_message events. 

# For New Plugins visit :

[![Plugins](https://img.shields.io/badge/Mrrobot-plugins-informational)](https://github.com/AKHACKER-program4hack/mrrobot-plugins)


## Credits, and Thanks to

*  [AKHACKER](https://github.com/AKHACKER-program4hack) Owner Of the Userbot. 

---




