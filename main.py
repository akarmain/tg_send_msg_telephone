import asyncio
import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')


async def send_message(receiver, txt_msg):
    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.send_message(receiver, txt_msg)


if __name__ == '__main__':
    number_order = 123

    user_name_or_id = "akarmain"
    text_msg = 'Hello World!\n\n autor @akarmain' + number_order
    asyncio.run(send_message(user_name_or_id, text_msg))
