import configparser

config = configparser.ConfigParser()
config.read("secrets.ini")

print(config['DISCORD']['user'])
