import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from ZedzeX import app

import config
from ZedzeX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    zedze = math.floor(percentage)
    if 0 < zedze <= 2:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 2 < zedze < 3:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 3 <= zedze < 4:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 4 <= zedze < 5:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 6 <= zedze < 7:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 7 <= zedze < 8:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 9 <= zedze < 10:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 11 <= zedze < 12:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 12 <= zedze < 13:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 13 < zedze < 14:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 14 <= zedze < 15:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 15 <= zedze < 16:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 16 <= zedze < 17:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 17 <= zedze < 18:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 18 <= zedze < 19:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 19 <= zedze < 20:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 20 <= zedze < 21:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 21 <= zedze < 22:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 22 <= zedze < 23:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 23 <= zedze < 24:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 24 <= zedze < 25:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 25 <= zedze < 26:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 26 <= zedze < 27:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 27 <= zedze < 28:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 28 <= zedze < 29:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 29 <= zedze < 30:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 30 <= zedze < 31:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 31 <= zedze < 32:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 32 <= zedze < 33:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 33 <= zedze < 34:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 34 <= zedze < 35:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 35 <= zedze < 36:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 36 <= zedze < 37:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 37 <= zedze < 38:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 38 <= zedze < 39:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 39 <= zedze < 40:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 40 <= zedze < 41:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 41 <= zedze < 42:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 42 <= zedze < 43:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 43 <= zedze < 44:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 44 < zedze < 45:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 45 <= zedze < 46:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 46 <= zedze < 47:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 47 <= zedze < 48:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 48 <= zedze < 49:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 49 <= zedze < 50:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 50 <= zedze < 51:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 51 <= zedze < 52:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 52 <= zedze < 53:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 53 <= zedze < 54:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 54 <= zedze < 55:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 55 <= zedze < 56:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 56 <= zedze < 57:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 57 <= zedze < 58:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 58 <= zedze < 59:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 59 <= zedze < 60:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 60 <= zedze < 61:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 61 <= zedze < 62:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 62 <= zedze < 63:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 63 <= zedze < 64:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 64 <= zedze < 65:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 65 <= zedze < 66:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 66 <= zedze < 67:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 67 <= zedze < 68:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 68 <= zedze < 69:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 69 <= zedze < 70:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 70 <= zedze < 71:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 71 <= zedze < 72:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 72 <= zedze < 73:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 73 <= zedze < 74:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 74 <= zedze < 75:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 75 <= zedze < 76:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 76 < zedze < 77:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 77 <= zedze < 78:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 78 <= zedze < 79:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 79 <= zedze < 80:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 80 <= zedze < 81:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 81 <= zedze < 82:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 82 <= zedze < 83:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 83 <= zedze < 84:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 84 <= zedze < 85:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 85 <= zedze < 86:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 86 <= zedze < 87:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 87 <= zedze < 88:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 88 <= zedze < 89:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 89 <= zedze < 90:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 90 <= zedze < 91:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 91 <= zedze < 92:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 92 <= zedze < 93:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 93 <= zedze < 94:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 94 <= zedze < 95:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 95 <= zedze < 96:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 96 <= zedze < 97:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 97 <= zedze < 98:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 98 <= zedze < 99:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    else:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"

        buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{dur} {bar} {played}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="★ σωиєя ★", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    zedze = math.floor(percentage)
    if 0 < zedze <= 2:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 2 < zedze < 3:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 3 <= zedze < 4:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 4 <= zedze < 5:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 6 <= zedze < 7:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 7 <= zedze < 8:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 9 <= zedze < 10:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 11 <= zedze < 12:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 12 <= zedze < 13:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 13 < zedze < 14:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 14 <= zedze < 15:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 15 <= zedze < 16:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 16 <= zedze < 17:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 17 <= zedze < 18:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 18 <= zedze < 19:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 19 <= zedze < 20:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 20 <= zedze < 21:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 21 <= zedze < 22:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 22 <= zedze < 23:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 23 <= zedze < 24:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 24 <= zedze < 25:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 25 <= zedze < 26:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 26 <= zedze < 27:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 27 <= zedze < 28:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 28 <= zedze < 29:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 29 <= zedze < 30:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 30 <= zedze < 31:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 31 <= zedze < 32:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 32 <= zedze < 33:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 33 <= zedze < 34:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 34 <= zedze < 35:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 35 <= zedze < 36:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 36 <= zedze < 37:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 37 <= zedze < 38:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 38 <= zedze < 39:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 39 <= zedze < 40:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 40 <= zedze < 41:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 41 <= zedze < 42:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 42 <= zedze < 43:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 43 <= zedze < 44:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 44 < zedze < 45:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 45 <= zedze < 46:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 46 <= zedze < 47:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 47 <= zedze < 48:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 48 <= zedze < 49:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 49 <= zedze < 50:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 50 <= zedze < 51:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 51 <= zedze < 52:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 52 <= zedze < 53:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 53 <= zedze < 54:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 54 <= zedze < 55:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 55 <= zedze < 56:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 56 <= zedze < 57:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 57 <= zedze < 58:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 58 <= zedze < 59:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 59 <= zedze < 60:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 60 <= zedze < 61:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 61 <= zedze < 62:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 62 <= zedze < 63:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 63 <= zedze < 64:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 64 <= zedze < 65:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 65 <= zedze < 66:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 66 <= zedze < 67:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 67 <= zedze < 68:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 68 <= zedze < 69:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 69 <= zedze < 70:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 70 <= zedze < 71:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 71 <= zedze < 72:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 72 <= zedze < 73:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 73 <= zedze < 74:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 74 <= zedze < 75:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 75 <= zedze < 76:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 76 < zedze < 77:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 77 <= zedze < 78:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 78 <= zedze < 79:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 79 <= zedze < 80:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 80 <= zedze < 81:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 81 <= zedze < 82:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 82 <= zedze < 83:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 83 <= zedze < 84:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 84 <= zedze < 85:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 85 <= zedze < 86:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 86 <= zedze < 87:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 87 <= zedze < 88:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 88 <= zedze < 89:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 89 <= zedze < 90:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 90 <= zedze < 91:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 91 <= zedze < 92:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 92 <= zedze < 93:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 93 <= zedze < 94:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 94 <= zedze < 95:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 95 <= zedze < 96:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 96 <= zedze < 97:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 97 <= zedze < 98:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 98 <= zedze < 99:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    else:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
        
        buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{dur} {bar} {played}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
           InlineKeyboardButton(
                text="🌿σωиєя🌿", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="★ σωиєя ★", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="★ σωиєя ★", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


## Search Query Inline


def track_markup(_,chat_id, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌿σωиєя🌿", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
        [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌿σωиєя🌿", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, chat_id, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ZedzePlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ZedzePlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌿σωиєя🌿", url="https://t.me/ALONE_WAS_BOT"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
    ]
    return buttons
