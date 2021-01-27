import discord
from .Controller import Controller

class NickBot(discord.Client):
    control = Controller()
    async def on_ready(self):
        print('Logged on as', self.user)
        await message.channel.send(self.control.get_prompt())

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.author == "Naseus":
            if message.content == 'hint':
                await message.channel.send(control.get_prompt())

            res = control.get_response(message.content)
            if res:
                await message.channel.send(res)

