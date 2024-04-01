from aiogram import types
from telethon import TelegramClient
from config_data.config import load_config, Config

config: Config = load_config()

client = TelegramClient(session=config.tg_bot.session, 
                        api_id=config.tg_bot.id, 
                        api_hash=config.tg_bot.hash, 
                        system_version = '4.16.30-vxCUSTOM')

# async def filter_megagroup(link) -> bool:
#     async with client:
#         return await client.get_entity(link).megagroup

async def filter_megagroup(message: types.Message) -> bool:
    async with client:
        try:
            entity = await client.get_entity(message.text)
            return entity.megagroup
        except Exception as e:
            print(f"Error checking megagroup: {e}")
            return False
