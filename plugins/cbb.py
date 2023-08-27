#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> Bot Creator :</b> <a href='https://t.me/ruban9124'> ❤️‍🔥 𝘿𝙖𝙚𝙣𝙚𝙧𝙮𝙨 𝙏𝙖𝙧𝙜𝙖𝙧𝙮𝙚𝙣 ❤️‍🔥 </a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("🎬 MAIN CHANNEL 🎬", url="https://t.me/+3GaGceTcxUwyNjhl"),
                     InlineKeyboardButton("🔒 CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
