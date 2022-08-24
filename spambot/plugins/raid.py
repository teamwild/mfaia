import random
from spambot import *
from spambot.helpers.gspam import GSPAM
from telethon import events


myraid = False
fraid = False

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/mraid'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/mraid'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/mraid'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/mraid'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/mraid'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/mraid'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/mraid'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/mraid'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/mraid'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/mraid'))
async def mraid(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        me = await e.client.get_me()
        global myraid
        if e.is_reply is True:
            replied = await e.get_reply_message()
            get_name = replied.sender.first_name
            get_id = replied.sender.id
            tag = f"[{get_name}](tg://user?id={get_id})"
            try:
                if get_id in GOD_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Kid!` {tag} `Is You're Daddy! You Cant Abuse Him!`")
                elif get_id in DEV_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Dev User!`")
                elif get_id == OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Master!`")
                elif get_id in CO_OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Co-Owner!`")
                elif get_id  in SUDO_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Sudo User!`")
                elif get_id == me.id:
                    await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                else:
                    await e.client.send_message(e.chat_id, f"`Mention Raid Activated On` {tag}!")
                    myraid = True
                    while myraid == True:
                        myMessage = random.choice(GSPAM)
                        await e.client.send_message(e.chat_id, f"{tag} {myMessage}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            text = e.raw_text[7:]
            try:
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Mention Raid!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    if get_id in GOD_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Kid!` {tag} `Is You're Daddy! You Cant Abuse Him!`")
                    elif get_id in DEV_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Dev User!`")
                    elif get_id == OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Master!`")
                    elif get_id in CO_OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Co-Owner!`")
                    elif get_id  in SUDO_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Sudo User!`")
                    elif get_id == me.id:
                        await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                    else:
                        await e.client.send_message(e.chat_id, f"`Mention Raid Activated On` {tag}!")
                        myraid = True
                        while myraid == True:
                            myMessage = random.choice(GSPAM)
                            await e.client.send_message(e.chat_id, f"{tag} {myMessage}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/sraid'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/sraid'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/sraid'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/sraid'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/sraid'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/sraid'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/sraid'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/sraid'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/sraid'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/sraid'))
async def sraid(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        global myraid
        if e.is_reply is True:
            try:
                replied = await e.get_reply_message()
                get_name = replied.sender.first_name
                get_id = replied.sender.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                myraid = False
                await e.client.send_message(e.chat_id, f"`Mention Raid Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            try:
                text = e.raw_text[7:]
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Deactivate Mention Raid!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    myraid = False
                    await e.client.send_message(e.chat_id, f"`Mention Raid Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
 
@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/raid'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/raid'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/raid'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/raid'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/raid'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/raid'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/raid'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/raid'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/raid'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/raid'))
async def raid(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        global fraid
        fraid = True
        await e.client.send_message(e.chat_id, "`Raid Activated Successfully`")
        while fraid == True:
            myMessage = random.choice(GSPAM)
            await e.client.send_message(e.chat_id, myMessage)


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/draid'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/draid'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/draid'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/draid'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/draid'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/draid'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/draid'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/draid'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/draid'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/draid'))
async def draid(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        global fraid
        fraid = False
        await e.client.send_message(e.chat_id, "`Raid Deactivated Successfully`")
