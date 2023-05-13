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
    if 0 < anon <= 10:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 10 < anon < 20:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 20 <= anon < 30:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 30 <= anon < 40:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 40 <= anon < 50:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 50 <= anon < 60:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 60 <= anon < 70:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 70 <= anon < 80:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 80 <= anon < 95:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    else:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"

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


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    zedze = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 10 < anon < 20:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 20 <= anon < 30:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 30 <= anon < 40:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 40 <= anon < 50:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 50 <= anon < 60:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 60 <= anon < 70:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 70 <= anon < 80:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 80 <= anon < 95:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    else:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
        
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
