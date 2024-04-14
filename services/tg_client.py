from telethon import TelegramClient  #type: ignore
from config_data.config_queue import config_queue
 
id, hash, session = config_queue.get()

client = TelegramClient(session=session, 
                        api_id=id, 
                        api_hash=hash, 
                        system_version = '4.16.30-vxCUSTOM')
