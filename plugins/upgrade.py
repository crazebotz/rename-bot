"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/TgContact_bot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited
	Price Rs 99  🇮🇳/🌎 2$  per Month
	
	
	Pay Using Upi I'd ```rahulji.7@ybl```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP** 
	Daily  Upload  limit unlimited 
	Price Rs 99  🇮🇳/🌎 2$  per Month
	
	
	Pay Using Upi I'd ``rahulji.7@ybl``
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	await message.reply_text(text = text,reply_markup = keybord)
