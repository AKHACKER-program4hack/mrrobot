import os
import sys
import pathlib
import psutil
from pyrogram import Client

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
USERBOT_SESSION = os.environ.get("USERBOT_SESSION", None)


class UserBot(Client):
    file_path = pathlib.Path(__file__).parent
    main_directory = str(file_path.parent)
    def __init__(self, name):
        name = name.lower()

        super().__init__(
            USERBOT_SESSION,# if USERBOT_SESSION is not None else name,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root=f"{name}/plugins"),
            workdir="./",
            app_version="Userbot v1.0",
        )

    async def start(self):
        await super().start()
        await super().send_message("me", "Userbot started")

        print("Userbot started. Hi.")

    async def stop(self, *args):
        await super().stop()
        print("Userbot stopped. Bye.")

    async def restart(self, *args, git_update=False, pip=False):
        """ Shoutout to the Userg team for this."""
        await self.stop()
        try:
            c_p = psutil.Process(os.getpid())
            for handler in c_p.open_files() + c_p.connections():
                os.close(handler.fd)
        except Exception as c_e:
            print(c_e)

        if git_update:
            os.system("git reset --hard")
            os.system("git pull")
        if pip:
            os.system("pip install -U -r requirements.txt")

        os.execl(sys.executable, sys.executable, "-m", self.__class__.__name__.lower())
        sys.exit()
