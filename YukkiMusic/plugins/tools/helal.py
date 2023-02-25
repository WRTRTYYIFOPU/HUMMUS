import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر    
@app.on_message(
    filters.command(["سورس","السورس"],""))
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10dfb95793ff3d40e0a90.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [ᴋɪʙʀɪᴀ¹](t.me/FH_KN) \n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝚁𝙰𝚂𝙺𝙾²](t.me/AA969622) \n• ᴄʜᴀɴɴᴇʟ 𝙻𝙸𝙽𝙳𝙰 » [ᴄʜᴀɴɴᴇʟ](t.me/A1122ll)\n\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♔ ֆۦ𓆩™𓆪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )     
@app.on_message(
    filters.command(["الاوامر"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/15ab2ecef4cc16d95be30.jpg",
        caption=f"""𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {message.from_user.mention}
        
« اليك قائـمة الاوامــر »
          

» لتشغيل اغنيه اكتب : تشغيل او شغل
» لأنهاء الاغنيه اكتب : ايقاف او انهاء 
» لايقاف الاغنيه مؤقت اكتب : قف 
» لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر
» لتخطي الاغنيه اكتب : تخطي او التالي
» لكتم البوت في المحادثه اكتب : ڪتم او اسكتي
» لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي
» لتحميـل الاغانـي اڪتب : بحث او تحميل
» لاعادة تشغيل البوت اكتب : /restart""

اوامـر التشغيـل.""",
      reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♔ ֆۦ𓆩™𓆪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )  
@app.on_message(
    filters.command(["مطور","المطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cda29519fd4604624777b.jpg",
        caption=f"""ᴡᴇʟᴄᴏᴍᴇ 
╭──── • ◈ • ────╮
» [ᴄʜᴀɴɴᴇʟ ](t.me/FH_KP)
» [ᴅᴇᴠᴇʟᴏᴘᴇʀ](t.me/cf222)
╰──── • ◈ • ────╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("وتيٌـِـ¦ـنَ الروحُ ♔ ֆۦ𓆩™𓆪", url=f"https://t.me/FH_KP")
                ]
            ]
        ),
    )      