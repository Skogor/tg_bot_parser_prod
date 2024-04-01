from telethon import TelegramClient
from config_data.config import load_config, Config

config: Config = load_config()

client = TelegramClient(session=config.tg_bot.session, 
                        api_id=config.tg_bot.id, 
                        api_hash=config.tg_bot.hash, 
                        system_version = '4.16.30-vxCUSTOM')
