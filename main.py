from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
import logging
import asyncio

async def main():
    logging.basicConfig(level=logging.INFO)

    config: Config = load_config() 

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
