from spambot import *
from telethon import events
from datetime import datetime

PING = """
█▀█  █  █▄░█  █▀▀  █
█▀▀  █  █░▀█  █▄█  ▄                                                               
"""

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/ping'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/ping'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/ping'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/ping'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/ping'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        before = datetime.now()
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"{PING}\n🔰 ᴍᴀꜰɪᴀ ꜱᴘᴀᴍ ᴜꜱᴇʀʙᴏᴛ 🔰\n\n➠ ᴍʏ ᴍᴀꜱᴛᴇʀ:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\n➠ ᴘɪɴɢ:- {ms} ms\n\n⚜️ 𝐌𝐚𝐟𝐢𝐚 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭 𝐎𝐧 𝐅𝐢𝐫𝐞 ⚜️")
