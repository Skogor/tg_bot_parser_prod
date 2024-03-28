from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    id: int
    hash: str
    session: str

@dataclass
class Config:
    tg_bot: TgBot

env = Env()
env.read_env()

config = Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                             id=env('API_ID'),
                             hash=env('API_HASH'),
                             session=env('SESSION')))

print('BOT_TOKEN - ', config.tg_bot.token)