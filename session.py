##Pyrogram string session

import asyncio
from pyrogram import Client

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")

with Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as app:
    app.send_message(
            "me",
            "**هذا هو كود السيشن الخاص بك يستعمل للتنصيب احذر مشاركته لأشخاص ليسوا أهل ثقة قد يتسبب بأختراق حسابك**\n\n"
            f"`{app.export_session_string()}`"
        )
    print(
            "Done, your Pyrogram session string has been sent to "
            "Saved Messages of your Telegram account!"
        )
