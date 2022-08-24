from spambot import *
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={int(OWNER_ID)})"


alive_msg = f"""
🔥⚡𝐌𝐚𝐟𝐢𝐚 𝐒𝐩𝐚𝐦 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐢𝐯𝐞!⚡🔥

➠ ᴍʏ ᴍᴀꜱᴛᴇʀ:- {master}

➠ ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:- `{BOT_VERSION}`

➠ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ:- `{version.__version__}`

⚜️ {BIO_MSG} ⚜️
"""

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/alive'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/alive'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/alive'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/alive'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/alive'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/alive'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.delete()
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)
