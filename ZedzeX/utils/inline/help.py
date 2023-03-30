from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ 𝐀𝐝𝐦𝐢𝐧 ✯",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="✯ 𝐀𝐮𝐭𝐡 ✯",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✯ 𝐁𝐥𝐚𝐜𝐤𝐥𝐢𝐬𝐭 ✯",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="✯ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 ✯",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✯ 𝐆𝐛𝐚𝐧 ✯",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="✯ 𝐋𝐲𝐫𝐢𝐜𝐬 ✯",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✯ 𝐏𝐢𝐧𝐠 ✯",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="✯ 𝐏𝐥𝐚𝐲 ✯",
                    callback_data="help_callback hb8",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✯ 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 ✯",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="✯ 𝐕𝐢𝐝𝐞𝐨 𝐂𝐡𝐚𝐭 ✯",
                    callback_data="help_callback hb10",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✯ 𝐒𝐭𝐚𝐫𝐭 ✯",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="✯ 𝐒𝐮𝐝𝐨 ✯",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"🔐 𝗖𝗹𝗼𝘀𝗲"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ 𝐇𝐞𝐥𝐩 ✯",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
