import configparser
import discord

config = configparser.ConfigParser()
config.read("secrets.ini")


class NickBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = NickBot()
client.run(config['DISCORD']['bot_token'])
