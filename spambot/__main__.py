import glob
from pathlib import Path
from sys import argv
from spambot import *
from spambot.utils import load_plugs


if __name__ == "__main__":
    modules = "spambot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import spambot
import spambot.userNeeds
import spambot.help
import spambot.helpers.callbackQuery


print("\n\nMafia Spam Userbot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        MafiaBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot5.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        MafiaBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot.run_until_disconnected()
    except Exception as e:
        print(e)
        pass