import telethon
from telethon import Button
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio
import re
import os
import sys
from asyncio.exceptions import CancelledError
from config import *
import logging
import asyncio
import time
from time import sleep
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup
import requests
import random
a = requests.session()
bot_username =	'@dam3ombot'
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("shahm")
logger.info("سورس التجميع والنشر  شغال الان استمتع بالتجميع✓")
DEVS = [6066647930]
onerabbas_id = (int(DEVLOO))
abbas.start()
@abbas.on(events.NewMessage)
async def join_channel(event):
	try :
		await abbas(JoinChannelRequest('@SHA_HM1'))
	except BaseException:
		pass		
@abbas.on(events.NewMessage)
async def join_channel(event):
	try:
		await abbas(JoinChannelRequest('@SHA_HM3'))
	except BaseException :
		pass
@abbas.on(events.NewMessage)
async def join_channel(event):
	try:
		await abbas(JoinChannelRequest('@Super_Shahm'))
	except BaseException :
		pass

@abbas.on(events.NewMessage)
async def join_channel(event):
	try:
		await abbas(JoinChannelRequest('@lggbg'))
	except BaseException :
		pass
@abbas.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def onerstart(event):
	sender = await event.get_sender()
	if sender.id == onerabbas_id:
		order = await event.reply('السورس يعمل بنجاح حبيبي ')
@abbas.on(events.NewMessage(outgoing=False, pattern='.دعمكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == onerabbas_id:
        await event.reply("جاري تجميع النقاط")
        #
        channel_entity = await abbas.get_entity(bot_username)
        await abbas.send_message(bot_username, '/start')
        await asyncio.sleep(2)
        msg0 = await abbas.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await abbas.get_messages(bot_username, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await abbas(GetHistoryRequest(peer=channel_entity, limit=1,                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await shahm1.send_message(event.chat_id, f"تم الانتهاء من التجميع | SH")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await abbas(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await abbas(ImportChatInviteRequest(bott))
                msg2 = await abbas.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.reply(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await abbas.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.reply(f"القناة رقم {chs}")
        await abbas.send_message(event.chat_id, "تم الانتهاء من التجميع | SH")

abbas.run_until_disconnected()