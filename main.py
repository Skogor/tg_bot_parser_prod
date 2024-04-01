from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from keyboards.main_menu import set_main_menu
from handlers import user_handlers
from services.tg_client import client
import logging
import asyncio

async def main():
    logging.basicConfig(level=logging.INFO)

    config: Config = load_config() 

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()
    
    #запуск клиента telegram
    await client.start()

    #использование workflow_data диспетчера для прокидывания конф. данных в другие модули (фильтры, роутеры)
    tkn = config.tg_bot.token
    tel_id = config.tg_bot.id
    tel_hash = config.tg_bot.hash
    tel_session = config.tg_bot.session

    dp.workflow_data.update({'my_token': tkn, 'my_id': tel_id, 'my_hash': tel_hash, 'my_session': tel_session})

    #инициализация menu
    await set_main_menu(bot)

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    asyncio.run(main())
