import asyncio
from telethon.sessions import StringSession
from telethon import TelegramClient

api_id = 2184829
api_hash = "6930b92388baabff4cb4a1d377085035"

async def main():
    async with TelegramClient(StringSession(), api_id=api_id, api_hash=api_hash) as MafiaBot:
        string = MafiaBot.session.save()
        print(string)
        await MafiaBot.send_message("me", f"Mafia Spam Userbot String Session👇👇\n\n`{string}`\n\n[🔥⚡MafiaBot Support⚡🔥](t.me/MafiaBot_Support)")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())