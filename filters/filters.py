from aiogram import types
from services.tg_client import client


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
