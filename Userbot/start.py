from datetime import datetime
from sys import version_info
from pyrogram.types import Message

from config import (
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Userbot.helpers.fsub import forcesubs
from config import HNDLR, bot, call_py
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)


@Client.on_message(
    filters.command(["start"], prefixes=f"{HNDLR}"))
@forcesubs
async def start(client, m: Message):
      await m.reply(
        f"""✨ **Selamat datang {m.from_user.mention()} !**\n
💭 [{ʙɪɴᴀʀʏ ᴍᴜsɪᴄ}](https://t.me/BinaryUserMusic) **Memungkinkan Anda memutar musik & video di grup melalui obrolan video Telegram!**

💡 **Temukan semua perintah Bot dan cara kerjanya dengan mengklik » 📚 [Perintah!](https://t.me/ChannelBinary/38)**

🔖 **Semua perintah dapat digunakan dengan » ; **
""",
)
