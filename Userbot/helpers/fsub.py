from typing import Callable
from pyrogram import Client
from pyrogram.types import Message,InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from config import FORCESUB as force

def forcesubs(func : Callable) -> Callable:
    async def wrapper(c, m):
        if force:
            try:
                chat = await c.get_chat_member(force,m.from_user.id)

                if chat.status=='kicked':
                    return await m.reply_text('Kamu Telah di Ban dari Channel Jadi Ngga bisa ๐๐๐๐คฃ๐คฃ๐คฃ๐๐๐',  quote=True)
            except UserNotParticipant:
                user_id = m.from_user.id
                user_name = m.from_user.first_name
                rpk = "["+user_name+"](tg://user?id="+str(user_id)+")" 
                button = [
                            [
                                InlineKeyboardButton('สษชษดแดสส แดสแดแดแดแดแด', url=f'https://t.me/{force}')
                            ]
                        ]
                markup = InlineKeyboardMarkup(button)
                return await m.reply_text(text=f"โจ **Halo {rpk}**\n** Hanya Yang Sudah Subs Channel Binary Music yang dapat menggunakan Bot Music ini ๐**\n"
                    "\nโก **Klik @BinarySupport Untuk Join Channel Binary Music**__", parse_mode='markdown', reply_markup=markup, quote=True)
            return await func(c, m)
    return wrapper
