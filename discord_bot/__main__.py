import configparser
from .bot import NickBot
from  pathlib import Path

config = configparser.ConfigParser()

config.read(Path(Path(__file__).parent, 'secrets.ini'))

user = config['DISCORD']['user']

if __name__ == '__main__':
    client = NickBot(user)
    client.run(config['DISCORD']['bot_token'])
