import random
from spambot import *
from spambot.helpers.plinks import PLINKS
from telethon import events

a = False

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/pspam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/pspam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/pspam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/pspam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/pspam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/pspam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/pspam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/pspam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/pspam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/pspam'))
async def pspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        await e.delete()
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        elif e.raw_text[6:] == "":
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        
@MafiaBot1.on(events.NewMessage(outgoing=True, pattern="/pstop"))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern="/pstop"))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern="/pstop"))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern="/pstop"))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern="/pstop"))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern="/pstop"))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern="/pstop"))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern="/pstop"))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern="/pstop"))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern="/pstop"))
async def pstop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.delete()
        await e.client.send_message(e.chat_id, "Porn Spam Stopped Successfully")