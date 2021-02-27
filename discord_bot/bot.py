import discord
from .Controller import Controller

class NickBot(discord.Client):
    def __init__(self, tu):
        super().__init__()
        self.target_user = tu
        self.control = Controller()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        print(message)

        if message.author.name == self.target_user:
            if message.content == 'hint':
                await message.channel.send(self.control.get_prompt())

            res = self.control.get_response(message.content)
            if res:
                print(res)
                await message.channel.send(res)

