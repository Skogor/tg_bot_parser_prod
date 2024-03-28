from aiogram import Bot, Dispatcher
from config_data.config import load_config

config = load_config()

bot = Bot(config.tg_bot.token)
dp = Dispatcher()

#использование workflow_data диспетчера для прокидывания конф. данных в другие модули
tkn = config.tg_bot.token
tel_id = config.tg_bot.id
tel_hash = config.tg_bot.hash
tel_session = config.tg_bot.session

dp.workflow_data.update({'my_token': tkn, 'my_id': tel_id, 'my_hash': tel_hash, 'my_session': tel_session})

print(dp.workflow_data)
