from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	username = user.username  # Get the username of the bot
	if username:
		mention = f"@{username}"  # Create a mention using the bot's username
	else:
		mention = "your bot"  # Default mention if username is not available
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons)
	)
	await bot.send_message(
		msg.chat.id,
		'Use below buttons to interact with me',
		reply_markup=ReplyKeyboardMarkup(
			[
				['+ Add Channels +'],
				['Manage Channels'],
				['Report a Problem']
			],
			one_time_keyboard=True,
			resize_keyboard=True
		)
	)
