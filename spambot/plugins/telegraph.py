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
                    await e.client.send_message(e.chat_id, f"๐ฑ ๐๐๐๐ข๐๐๐จ๐ญ ๐๐๐ฅ๐๐ ๐ซ๐๐ฉ๐ก ๐๐๐๐ข๐๐ฑ \n\nโ  สษชษดแด:- {upload}\n\nโ  แดษชแดแด แดแดแดแดษด:- `{response[:4]} ๊ฑแดแดแดษดแด๊ฑ!`\n\n")
                    os.remove(media)
            except Exception as er:
                print(str(er))
        else:
            await e.client.send_message(e.chat_id, "`Please Reply To Image Or Gif!`")
