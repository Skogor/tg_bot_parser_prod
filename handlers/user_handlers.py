from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from services.tg_client import client

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Добро пожаловать! Введите ссылку на чат!')

@router.message(F.text.startswith('https://t.me'))
@router.message(F.text.startswith('t.me'))
async def process_beginning_command(message: Message):
    entity = await client.get_entity(message.text)
    if entity.megagroup == False:
        await message.answer(text='Ссылка не является чатом!')
    else: await message.answer(text='Приступим!')

@router.message()
async def other(message: Message):
    await message.answer(text="Это не ссылка!")


    