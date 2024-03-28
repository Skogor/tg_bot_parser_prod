from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from keyboards.main_menu import set_main_menu
from handlers import user_handlers
import logging
import asyncio

async def main():
    logging.basicConfig(level=logging.INFO)

    config: Config = load_config() 

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
