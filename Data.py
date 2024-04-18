from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

By @XAYOONARA
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏴‍☠ ʜᴏᴍᴇ 🏴‍☠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ sᴜᴘᴘᴏʀᴛ ✨", url="https://t.me/")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ❔", callback_data="help")
        ],
        [InlineKeyboardButton("🤖ᴜᴘᴅᴀᴛᴇs", url="https://t.me/")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @XAYOONARA
    """
