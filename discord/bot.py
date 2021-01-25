import configparser
import discord
from Controller import Controller

config = configparser.ConfigParser()
config.read("secrets.ini")

control = Controller()

class NickBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'hint':
            await message.channel.send(control.get_prompt())

        res = control.get_response(message.content)
        if res:
        	await message.channel.send(res)
client = NickBot()
client.run(config['DISCORD']['bot_token'])
