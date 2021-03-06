import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("â¡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>ð PONG</b> `{delta_ping * 1000:.3f} ms` \n<b>â³ AKTIF</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**â Userbot Di Restart Ulang**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>ð Hallo {m.from_user.mention}!

ð  MENU BANTUAN [ÊÉªÉ´á´ÊÊ á´á´sÉªá´](https://t.me/BinaryUserMusic)

â¡ PERINTAH UNTUK SEMUA ORANG
â¢ {HNDLR}play (judul lagu) | untuk memutar lagu
â¢ {HNDLR}vplay judul video) | untuk memutar video
â¢ {HNDLR}playlist untuk melihat daftar putar
â¢ {HNDLR}ping - untuk cek status
â¢ {HNDLR}id - untuk melihat id pengguna
â¢ {HNDLR}video - judul video | link yt untuk mencari video
â¢ {HNDLR}song - judul lagu | link yt untuk mencari lagu
â¢ {HNDLR}help - untuk melihat daftar perintah
â¢ {HNDLR}join- untuk join | ke grup 

â¡ PERINTAH KHUSUS UNTUK SEMUA ADMIN
â¢ {HNDLR}resume - untuk melanjutkan pemutaran lagu atau video
â¢ {HNDLR}pause - untuk untuk menjeda pemutaran lagu atau video
â¢ {HNDLR}skip - untuk melewati lagu atau video
â¢ {HNDLR}end - untuk mengakhiri pemutaran</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>ð£ Lapor Bos {m.from_user.mention}!

â Barusan orang ini ngeklik tombol repo wkwkwkwk

"""
    await m.reply(REPO, disable_web_page_preview=True)
