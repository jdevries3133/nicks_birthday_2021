import logging
import configparser
from .bot import NickBot
from  pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
    format='%(pathname)s:%(lineno)s\n\t%(module)s::%(message)s'
)

config = configparser.ConfigParser()
config.read(Path(Path(__file__).parent, 'secrets.ini'))

user = config['DISCORD']['user']

client = NickBot(user)
client.run(config['DISCORD']['bot_token'])
