import logging
import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from config_data.config_queue import config_queue
from services.tg_client import client
from keyboards.main_menu import set_main_menu
from handlers import user_handlers


async def main():
    logging.basicConfig(level=logging.INFO)

    config: Config = load_config()

    #помещаем данные в очередь для прокидывания в TelegramClient
    config_queue.put((config.tg_bot.id, config.tg_bot.hash, config.tg_bot.session)) 

    #запуск клиента telegram
    await client.start()

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    #использование workflow_data диспетчера для прокидывания конф. данных в другие модули (фильтры, роутеры)
    tkn = config.tg_bot.token
    tel_id = config.tg_bot.id
    tel_hash = config.tg_bot.hash
    tel_session = config.tg_bot.session

    dp.workflow_data.update({'my_token': tkn, 'my_id': tel_id, 'my_hash': tel_hash, 'my_session': tel_session})

    #инициализация menu
    await set_main_menu(bot)

    #регистрация роутеров в диспетчере
    dp.include_router(user_handlers.router)

    #пропуск накопившихся апдейтов и запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    asyncio.run(main())
