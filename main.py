import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient('anon', api_id, api_hash)


async def main():
    me = await client.get_me()
    print(me.stringify())
    print(me.phone)
    await client.send_message("me", '200 ok')


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
