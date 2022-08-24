import random
from spambot import *
from spambot.helpers.gspam import GSPAM
from spambot.helpers.plinks import PLINKS
from telethon import events

myraid = False
myspam = False
a = False

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/dmraid'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/dmraid'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/dmraid'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/dmraid'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/dmraid'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/dmraid'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/dmraid'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/dmraid'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/dmraid'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/dmraid'))
async def dmraid(e):
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
                    await e.client.send_message(e.chat_id, f"`Dm Raid Activated On` {tag}!")
                    myraid = True
                    while myraid == True:
                        myMessage = random.choice(GSPAM)
                        await e.client.send_message(get_id, f"{myMessage}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            text = e.raw_text[8:]
            try:
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Dm Raid!")
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
                        await e.client.send_message(e.chat_id, f"`Dm Raid Activated On` {tag}!")
                        myraid = True
                        while myraid == True:
                            myMessage = random.choice(GSPAM)
                            await e.client.send_message(get_id, f"{myMessage}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/sdmraid'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/sdmraid'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/sdmraid'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/sdmraid'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/sdmraid'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/sdmraid'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/sdmraid'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/sdmraid'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/sdmraid'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/sdmraid'))
async def sdmraid(e):
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
                await e.client.send_message(e.chat_id, f"`Dm Raid Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            try:
                text = e.raw_text[9:]
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Deactivate Dm Raid!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    myraid = False
                    await e.client.send_message(e.chat_id, f"`Dm Raid Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/dmspam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/dmspam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/dmspam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/dmspam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/dmspam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/dmspam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/dmspam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/dmspam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/dmspam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/dmspam'))
async def dmspam(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        me = await e.client.get_me()
        global myspam
        if e.is_reply is True:
            replied = await e.get_reply_message()
            replied_message = replied.message            
            text = e.raw_text[8:]
            try:
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Dm Spam!")
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
                        await e.client.send_message(e.chat_id, f"`Dm Spam Activated On` {tag}!")
                        myspam = True
                        while myspam == True:
                            await e.client.send_message(get_id, f"{replied_message}")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/sdmspam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/sdmspam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/sdmspam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/sdmspam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/sdmspam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/sdmspam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/sdmspam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/sdmspam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/sdmspam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/sdmspam'))
async def sdmspam(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        global myspam
        if e.is_reply is True:
            try:
                replied = await e.get_reply_message()
                get_name = replied.sender.first_name
                get_id = replied.sender.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                myspam = False
                await e.client.send_message(e.chat_id, f"`Dm Spam Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            try:
                text = e.raw_text[9:]
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Deactivate Dm Spam!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    myspam = False
                    await e.client.send_message(e.chat_id, f"`Dm Spam Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/dmpspam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/dmpspam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/dmpspam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/dmpspam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/dmpspam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/dmpspam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/dmpspam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/dmpspam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/dmpspam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/dmpspam'))
async def dmpspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        await e.delete()
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        me = await e.client.get_me()
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            text = e.raw_text[9:]
            if text == "":
                await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Porn Spam In Dm!")
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
                    await e.client.send_message(e.chat_id, f"`Porn Spam In Dm Activated On` {tag}!")              
                try:
                    while a == True:
                        p = random.choice(PLINKS)
                        await e.client.send_file(get_id, p, caption=replied_message)
                except Exception as er:
                    print(er)
                    await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to dmpspam!")
        else:
            text = e.raw_text[9:]
            if text == "":
                await e.client.send_message(e.chat_id, "Please Mention Someone To Activate Porn Spam In Dm!")
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
                    await e.client.send_message(e.chat_id, f"`Porn Spam In Dm Activated On` {tag}!")              
                try:
                    while a == True:
                        p = random.choice(PLINKS)
                        await e.client.send_file(get_id, p)
                except Exception as er:
                    print(er)
                    await e.client.send_message(e.chat_id, "Something Went Wrong")


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern="/dmpstop"))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern="/dmpstop"))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern="/dmpstop"))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern="/dmpstop"))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern="/dmpstop"))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern="/dmpstop"))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern="/dmpstop"))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern="/dmpstop"))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern="/dmpstop"))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern="/dmpstop"))
async def dmpstop(e):
     if e.sender_id in MY_USERS:
        await e.delete()
        global a
        if e.is_reply is True:
            try:
                replied = await e.get_reply_message()
                get_name = replied.sender.first_name
                get_id = replied.sender.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                a = False
                await e.client.send_message(e.chat_id, f"`Dm Porn Spam Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            try:
                text = e.raw_text[9:]
                if text == "":
                    await e.client.send_message(e.chat_id, "Please Mention Someone To Deactivate Dm Porn Spam!")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    a = False
                    await e.client.send_message(e.chat_id, f"`Dm Porn Spam Deactivated On` {tag}!")
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
