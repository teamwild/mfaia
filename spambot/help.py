from spambot import *
from telethon import events, Button

HELP = f"""
ʜᴇʏ![🤗]({DISPLAY_PIC}) ᴛʜɪꜱ ɪꜱ ᴍᴀꜰɪᴀ ꜱᴘᴀᴍ ᴜꜱᴇʀʙᴏᴛ.⚡

ʏᴏᴜ ᴄᴀɴ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ ᴀɴᴅ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ᴜꜱɪɴɢ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ.🔱

ꜰᴜᴄᴋ ʏᴏᴜʀ ᴠɪᴄᴛɪᴍꜱ ᴀɴᴅ ᴇɴᴊᴏʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅ ᴅᴏɴᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ꜱᴜᴘᴘᴏʀᴛ [ᴍᴀꜰɪᴀʙᴏᴛ](https://t.me/MafiaBot_Support).🔥
"""

Buttons = [
    Button.inline("❆ ᴀʟɪᴠᴇ ❆", b'alive'),
    Button.inline("❆ ᴘɪɴɢ ❆", b'ping')
], [
    Button.inline("❆ ʀᴀɪᴅ ❆", b'raid'),
    Button.inline("❆ ʀᴇᴘʟʏ ʀᴀɪᴅ ❆", b'replyraid')
], [
    Button.inline("❆ ꜱᴘᴀᴍ ❆", b'spam'),
    Button.inline("❆ ᴘꜱᴘᴀᴍ ❆", b'pspam')
], [
    Button.inline("❆ ᴇxᴛʀᴀꜱ ❆", b'extras'),
    Button.inline("❆ ᴛᴇʟᴇɢʀᴀᴘʜ ❆", b'tm')
], [
    Button.inline("❆ ʙᴀɴ ᴀʟʟ ❆", b'ba'),
    Button.inline("❆ ᴅᴍ ʀᴀɪᴅ ❆", b'dm')
], [
    Button.inline("❆ ʜᴇʀᴏᴋᴜ ❆", b"heroku")
], [
    Button.url("〚 ᴄʜᴀɴɴᴇʟ 〛", "t.me/MafiaBot_Support"),
    Button.url("〚 ɢʀᴏᴜᴘ 〛", "t.me/MafiaBot_ChitChat")
], [
    Button.url("〘 ᴄʀᴇᴀᴛᴏʀ 〙", "t.me/H1M4N5HU0P")
]

BACK = [
    Button.inline("「 ʙᴀᴄᴋ 」", b'back')
]

@MafiaBot.on(events.InlineQuery)
async def helper(hquery):
    if hquery.text == b'help':
        try:
            message = hquery.builder.article('Help', text=HELP, buttons=Buttons)
            await hquery.answer(message)
        except Exception as er:
            print(er)

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/help'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/help'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/help'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/help'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/help'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        try:
            message = await e.client.inline_query(BOT_USERNAME, b'help')
            await message[0].click(e.chat_id, reply_to=e.reply_to_msg_id, hide_via=True)
        except Exception as er:
            print(er)
        

