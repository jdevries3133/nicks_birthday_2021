import configparser
from .bot import NickBot
from  pathlib import Path

config = configparser.ConfigParser()

config.read(Path(Path(__file__).parent, 'secret.ini'))
for i in config:
    print(i)

user = config['DISCORD']['user']

if __name__ == '__main__':
    client = NickBot()
    client.run(config['DISCORD']['bot_token'])
