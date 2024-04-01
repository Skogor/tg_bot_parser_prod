from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from telethon.sync import TelegramClient
from config_data.config import load_config, Config
#from filters.filters import filter_megagroup

config: Config = load_config()

client = TelegramClient(session=config.tg_bot.session, 
                        api_id=config.tg_bot.id, 
                        api_hash=config.tg_bot.hash, 
                        system_version = '4.16.30-vxCUSTOM')

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Добро пожаловать! Введите ссылку на чат!')

@router.message(F.text.startswith('https://t.me'))
async def process_beginning_command(message: Message):
    await client.start()
    entity = await client.get_entity(message.text)
    if entity.megagroup == False:
        await message.answer(text='Ссылка не является чатом!')
    else: await message.answer(text='Приступим!')

@router.message()
async def other(message: Message):
    await message.answer(text="Это не ссылка!")


    