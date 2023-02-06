import os
import config
from pyrogram.errors import FloodWait
import asyncio
from pyrogram import Client ,filters
from helper.database import getid ,delete
import time
ADMIN =  Config.ADMIN
 

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...")
   ids = getid()
   tot = len(ids)
   success = 0 
   failed = 0 
   await ms.edit(f"Starting Broadcast ...\nSending Message To {tot} Users")
   for id in ids:
     try:
     	time.sleep(1)
     	await message.reply_to_message.copy(id)
     	success += 1 
     except:
     	failed += 1
     	delete({"_id":id})     	 
     	pass
     try:
     	await ms.edit( f"**Total:** `{tot}`\n**Success:** `{success}`\n**Failed:** `{failed}`" )
     except FloodWait as e:
     	await asyncio.sleep(t.x)
