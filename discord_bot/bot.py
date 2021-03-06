import logging

import discord
from .controller import Controller

logger = logging.getLogger(__name__)

class NickBot(discord.Client):
    def __init__(self, tu):
        super().__init__()
        self.target_user = tu
        self.control = Controller()

    async def on_ready(self):
        logger.info(f'Logged on as {self.user}')

    async def on_message(self, message):
        # don't respond to ourself
        if message.author == self.user:
            return

        logger.info(f'Message recieved: {message}')

        if message.author.name == self.target_user:
            await self.reply(message)

    async def reply(self, message):
        if message.content in ['hint', 'help', '--help', '-h']:
            await self.send_hint(message)
            return

        res = self.control.get_response(message.content)
        if res:
            logger.info(f'Sending response: {res}')
            await message.channel.send(res)

    async def send_hint(self, message):
        await message.channel.send(self.control.get_prompt())

