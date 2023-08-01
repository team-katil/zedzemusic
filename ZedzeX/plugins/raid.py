import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from ZedzeX.misc import SUDOERS
import config
from config import BANNED_USERS
from ZedzeX import LOGGER, app, userbot
from ZedzeX.core.call import Vip
from ZedzeX.plugins import ALL_MODULES
from ZedzeX.utils.database import get_banned_users, get_gbanned


@app.on_message(
    filters.command("vcraid")
    & filters.group
    & ~filters.edited
    & ~SUDOERS

@PlayWrapper
async def play_commnd(
    client,
    message: Message,
    _,
    chat_id,
):

try:
        await Zedze.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Zedze.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
