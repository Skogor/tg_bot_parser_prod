from config_data.config import load_config

config = load_config()

print(config.tg_bot.session)
