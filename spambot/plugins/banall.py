import asyncio
from spambot import *
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantsKicked,ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest

BAN = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,

)

UNBAN = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,

)
@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/banall'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/banall'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/banall'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/banall'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/banall'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/banall'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/banall'))
async def banall(e):
    if e.sender_id in MY_USERS:
        if not e.is_group:
            await e.client.send_message(e.chat_id, "Really!! Is This A Group?")
        else:
            try:
                await e.delete()
                await e.client.send_message(e.chat_id, "On It!!")
                noobs = await e.client.get_participants(e.chat_id, filter=ChannelParticipantsAdmins)
                cant_ban = [admin.id for admin in noobs]
                async for users in e.client.iter_participants(e.chat_id):
                    try:
                        if users.id not in cant_ban:
                            await e.client(EditBannedRequest(e.chat_id, users.id, BAN))
                            await asyncio.sleep(0.1)
                    except Exception as er:
                        print(str(er))
                await e.client.send_message(e.chat_id, "Well Done!!")
            except Exception as er:
                print(str(er))


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/unbanall'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/unbanall'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/unbanall'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/unbanall'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/unbanall'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/unbanall'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/unbanall'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/unbanall'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/unbanall'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/unbanall'))
async def unbanall(e):
    if e.sender_id in MY_USERS:
        if not e.is_group:
            await e.client.send_message(e.chat_id, "Really!! Is This A Group?")
        else:
            try:
                await e.delete()
                await e.client.send_message(e.chat_id, "On It!!")
                async for users in e.client.iter_participants(e.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
                    try:
                        await e.client(EditBannedRequest(e.chat_id, users, UNBAN))
                        await asyncio.sleep(0.1)
                    except Exception as er:
                        print(str(er))
                await e.client.send_message(e.chat_id, "Well Done!!")
            except Exception as er:
                print(str(er))




