import os
import time
from spambot import *
from telethon import events
from html_telegraph_poster import upload_image


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/tm'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/tm'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/tm'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/tm'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/tm'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/tm'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/tm'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/tm'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/tm'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/tm'))
async def tm(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        if e.is_reply is True:
            try:
                start = time.time()
                replied = await e.get_reply_message()
                media = await e.client.download_media(replied)
                if media.endswith(".webp"):
                    await e.client.send_message(e.chat_id, "`Please Reply To Image Or Gif!`")
                    os.remove(media)
                else:
                    upload = upload_image(media)
                    end = time.time()
                    sec = (end - start)
                    response = str(sec)
                    await e.client.send_message(e.chat_id, f"🔱 𝐌𝐚𝐟𝐢𝐚𝐁𝐨𝐭 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐌𝐞𝐝𝐢𝐚🔱 \n\n➠ ʟɪɴᴋ:- {upload}\n\n➠ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:- `{response[:4]} ꜱᴇᴄᴏɴᴅꜱ!`\n\n")
                    os.remove(media)
            except Exception as er:
                print(str(er))
        else:
            await e.client.send_message(e.chat_id, "`Please Reply To Image Or Gif!`")
