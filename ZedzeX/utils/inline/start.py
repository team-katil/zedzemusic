from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import GROUP_USERNAME, CHANNEL_USERNAME


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝗛𝗲𝗹𝗽 ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯ 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀 ✯", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
            
        ],
        [
            InlineKeyboardButton(
                text="۞ 𝐀𝙻𝙻 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ✯", url=f"https://t.me/{GROUP_USERNAME}",
            ),
            InlineKeyboardButton(
                text="✯ 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ✯", url=f"https://t.me/{CHANNEL_USERNAME}",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱ƨσʋяcɛ🌱",
                url=f"https://github.com/team-katil/zedzemusic",
            )
        ],
     ]
    return buttons
