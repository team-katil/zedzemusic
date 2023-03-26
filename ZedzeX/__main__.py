import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from ZedzeX import LOGGER, app, userbot
from ZedzeX.core.call import Zedze
from ZedzeX.plugins import ALL_MODULES
from ZedzeX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("ZedzeX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("ZedzeX").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ZedzeX.plugins." + all_module)
    LOGGER("ZedzeX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Zedze.start()
    try:
        await Zedze.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Zedze.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ZedzeX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Zedze.decorators()
    LOGGER("ZedzeX").info("Zedze Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("ZedzeX").info("Stopping Zedze Music Bot...")
