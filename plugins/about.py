import os
from config import Config
from pyrogram import Client, filters
token =  Config.TOKEN
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\n**Bot :-** @TGRenamer_Robot\n**Buy Subscription :-** @TGContact_Bot\n**Subscribe :-** https://youtube.com/technologyrk\n\n**Total Renamed File :-** {total_rename}\n**Total Size Renamed :-** {humanbytes(int(total_size))} ",disable_web_page_preview=True,quote=True)
