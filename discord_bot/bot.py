import logging

import discord
from .Controller import Controller

logger = logging.getLogger(__name__)

class NickBot(discord.Client):
    def __init__(self, tu):
        super().__init__()
        self.target_user = tu
        self.control = Controller()

    async def on_ready(self):
        logger.info(f'Logged on as {self.user}')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        logger.info(message)

        if message.author.name == self.target_user:
            if message.content == 'hint':
                await message.channel.send(self.control.get_prompt())

            res = self.control.get_response(message.content)
            if res:
                logger.info(res)
                await message.channel.send(res)

