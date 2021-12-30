import os

from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls


# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "!")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BinarySupport")

BOT_USERNAME = getenv("BOT_USERNAME", "BinaryUserMusic")
OWNER_NAME = getenv("OWNER_NAME", "Pranata_11")
BOT_NAME = getenv("BOT_NAME", "ʙɪɴᴀʀʏ ᴍᴜsɪᴄ")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BinarySupport")

# Fsubs #
FORCESUB = getenv("FORCESUB", "BinarySupport") if getenv("FORCESUB", "BinarySupport") else None


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Userbot"))
call_py = PyTgCalls(bot)
