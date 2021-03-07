import logging

import discord
from .controller import Controller

logger = logging.getLogger(__name__)

GENERAL_CHANNEL_ID = 802628301399130136

class NickBot(discord.Client):

    def __init__(self, target_user):
        super().__init__()
        self.target_user = target_user
        self.control = Controller()

    async def on_ready(self):
        """
        Send initial prompt.
        """
        logger.info(f'Logged on as {self.user}')
        channel = self.get_channel(GENERAL_CHANNEL_ID)
        if channel:
            await channel.send(
                self.control.get_prompt()
            )
        else:
            logger.error('Channel not found for initial prompt')

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
        logger.info(f'Sending response: {res}')
        await message.channel.send(res)

    async def send_hint(self, message):
        await message.channel.send(self.control.get_prompt())

