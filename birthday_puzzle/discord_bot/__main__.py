import logging
import configparser
from .bot import NickBot
from  pathlib import Path


logging.basicConfig(
    filename=Path(Path(__file__).parents[2], 'discord_bot.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s => %(message)s',
)


config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent, 'secrets.ini'))

user = config['DISCORD']['user']

client = NickBot(user)
client.run(config['DISCORD']['bot_token'])
