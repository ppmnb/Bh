from telethon.sync import TelegramClient

from telethon.sessions import StringSession

import os

APP_ID = os.environ.get("APP_ID", "18922496")

APP_HASH = os.environ.get("APP_HASH", "371d1dc33eccaa19bb0814a27bb98f3c")

BOT_USERNAME = os.environ.get("BOT_USERNAME", "aiibot")

session = os.environ.get("TERMUX")

SESSION = os.environ.get("TERMUX", "1BJWap1sBu58rWnjzGBpI0tJraDdQ3d21TdAYtaPCyRIAdEUjHy-LIsbxQww9yQ8SFSr5AZZxqZrRVJ6AHR5lDW04vCY1fDF8K74aFLVdv0CeccIDYxXwcB6lEnIOIA-GDuSIOEpUTaNUnZs70WL-Vyggh3g2vS4MFOmPsbzzxQAKmXGmdjG_YwcXaGUQYW75POT8yltbAN0DW4qu13kKrETgVVtMHVt2P_z2K1jbZXKsZImasmaP7D4NQWqQofEmYRW4kiv1Ah2rfLP-b9Q56T3u7kjqCT-oZVpXmRHj-uAH2GamQSlU--AlV5qR-yu2RZFC7iqbBVLTQWfxPGNAsVWathACBLc=")

token = os.environ.get("TOKEN", "5663892372:AAGeOm-sRiIETxstqPYMSgOhWnaDu0ZNSFE")

fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)

bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)

ispay = ['yes']

ispay2 = ['yes']

bot.start()
