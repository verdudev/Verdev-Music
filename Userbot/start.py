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
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Selamat datang {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Memungkinkan Anda memutar musik & video di grup melalui obrolan video Telegram!**

💡 **Temukan semua perintah Bot dan cara kerjanya dengan mengklik tombol» 📚 Perintah!**

🔖 **Semua perintah dapat digunakan dengan: ; **
""",
)
