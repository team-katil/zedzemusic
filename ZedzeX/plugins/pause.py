from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from ZedzeX import app
from ZedzeX.core.call import Zedze
from ZedzeX.utils.database import is_music_playing, music_off
from ZedzeX.utils.decorators import AdminRightsCheck
from ZedzeX.utils.inline import close_keyboard


@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Zedze.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
