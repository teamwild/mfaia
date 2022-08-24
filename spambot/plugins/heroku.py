import heroku3
from spambot import *
from telethon import events
from spambot.helpers.neko import paster


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/restart'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/restart'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/restart'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/restart'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/restart'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/restart'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/restart'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/restart'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/restart'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/restart'))
async def restart(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        if (HEROKU_API_KEY is not None) or (HEROKU_APP_NAME is not None):
            try:
                await e.client.send_message(e.chat_id, "`Restarting...`")
                heroku_conn = heroku3.from_key(HEROKU_API_KEY)
                app = heroku_conn.app(HEROKU_APP_NAME)
                app.restart()
            except Exception as er:
                print(er)
        else:
            await e.client.send_message(e.chat_id, "Please Put `HEROKU_APP_NAME` And `HEROKU_API_KEY` In Heroku Vars!")


@MafiaBot1.on(events.NewMessage(outgoing=True, pattern='/logs'))
@MafiaBot2.on(events.NewMessage(outgoing=True, pattern='/logs'))
@MafiaBot3.on(events.NewMessage(outgoing=True, pattern='/logs'))
@MafiaBot4.on(events.NewMessage(outgoing=True, pattern='/logs'))
@MafiaBot5.on(events.NewMessage(outgoing=True, pattern='/logs'))
@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/logs'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/logs'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/logs'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/logs'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/logs'))
async def restart(e):
    if e.sender_id in MY_USERS:
        await e.delete()
        if (HEROKU_API_KEY is not None) or (HEROKU_APP_NAME is not None):
            try:
                heroku_conn = heroku3.from_key(HEROKU_API_KEY)
                app = heroku_conn.app(HEROKU_APP_NAME)
                log = app.get_log()
                logs1 = await paster(log)
                paste = f"[Click Here To Check Logs]({logs1})"
                await e.client.send_message(e.chat_id, f"Mafia Spam Userbot Logs:- {paste}\n")  
            except Exception as er:
                print(er)
        else:
            await e.client.send_message(e.chat_id, "Please Put `HEROKU_APP_NAME` And `HEROKU_API_KEY` In Heroku Vars!")
