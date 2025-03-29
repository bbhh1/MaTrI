"""

❃ `{i}نشر` <الوقت بين الارسال> <عدد الارسال> <الرسالة>
    لـ نشر الرسالة بعدد معين في جيمع مجموعاتك لكن بين ارسال رسالة واخرى وقت معين جرب ارسل   `. انشرلي 2 5 مرحبا`
   
❃ `{i}ايقاف النشر`
   لـ ايقاف امر النشر في المجموعات

⚠️ أنتبه قد يؤدي استخدام هذا الامر بكثرة الى تقييد حسابك من مراسلة المستخدمين اذا قاموا بالتبليغ عنك.. 
"""

import asyncio
from .. import jmthon_cmd,jmdB, DEV_CHAT, LOG_CHAT, TAG_CHAT

@jmthon_cmd(pattern="نشر")
async def nshr(event):
    args = event.text.split(" ", 3)
    delay = float(args[1])
    count = int(args[2])
    msg = str(args[3])

    mirz = await event.eor("⌔∮ يتم النشر في جميع المجموعات الان")
    er = 0
    done = 0
    jmdB.set_key("NSHR", True)

    for i in range(count):
        if not jmdB.get_key("NSHR"):
            break
        async for x in event.client.iter_dialogs():
            if x.is_group:
                chat = x.id
                try:
                    if chat not in DEV_CHAT and chat not in TAG_CHAT and chat not in LOG_CHAT:
                        await event.client.send_message(chat, msg)
                        await asyncio.sleep(1)
                        done += 1
                except BaseException:
                    er += 1
        await mirz.edit(f"**⌔∮  تم بنجاح النشر الى ** `{done}` **من الدردشات ، خطأ في ارسال الى ** `{er}` **من الدردشات**")
        await asyncio.sleep(delay)


@jmthon_cmd(pattern="ايقاف (النشر|نشر)")
async def stop_nshr(e):
    if jmdB.get_key("NSHR"):
        jmdB.del_key("NSHR")
        await e.respond("**⌔∮ تم إيقاف النشر الوقتي بنجاح!**")
    else:
        await e.respond("**⌔∮أمر النشر ليس قيد التنفيذ حاليًا.**")
