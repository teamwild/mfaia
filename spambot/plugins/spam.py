from spambot import *
from telethon import events

a = False

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/spam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/spam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/spam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/spam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/spam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/spam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/spam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/spam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/spam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/spam'))
async def spam(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        try:
            text = e.raw_text
            counts = int(text[6:8])
            spam = text[8:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                    await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/bigspam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/bigspam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/bigspam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/bigspam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/bigspam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/bigspam'))
async def bigspam(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        try:
            text = e.raw_text
            counts = int(text[9:13])
            spam = text[14:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                            await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/mspam'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/mspam'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/mspam'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/mspam'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/mspam'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/mspam'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/mspam'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/mspam'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/mspam'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/mspam'))
async def mspam(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        try:
            text = e.raw_text
            counts = int(text[7:13])
            if e.is_reply == False:
                await e.client.send_message(e.chat_id, "Please reply to a media and enter how many times you want send that media!")
            elif e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.media
                for i in range(counts):
                    await e.client.send_file(e.chat_id, replied_message)
            else:
                await e.client.send_message(e.chat_id, "Some thing went wrong! Please reply to a media and enter how many times you want send that media!")
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Please enter how many times you want to spam in reply of media!")

@MafiaBot1.on(events.NewMessage(outgoing=True, pattern="/uspam"))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern="/uspam"))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern="/uspam"))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern="/uspam"))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern="/uspam"))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern="/uspam"))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern="/uspam"))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern="/uspam"))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern="/uspam"))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspam(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        
@MafiaBot1.on(events.NewMessage(outgoing=True, pattern="/ustop"))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern="/ustop"))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern="/ustop"))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern="/ustop"))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern="/ustop"))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern="/ustop"))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern="/ustop"))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern="/ustop"))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern="/ustop"))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern="/ustop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        global a
        a = False
        await e.client.send_message(e.chat_id, "U Spam Stopped Successfully")
