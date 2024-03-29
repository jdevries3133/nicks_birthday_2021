"""
Wrapper class for ClickSend API
"""

import json
from base64 import b64encode
from pathlib import Path
import logging

import requests

from .clicksend import ClickSend, Address
from .riddles import Riddler
from ..email_puzzles.emailer import EmailBot

logger = logging.getLogger(__name__)

with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
    secrets = json.load(jsonf)

class Mailer(EmailBot):
    """
    Listen on the email address but reply with physical letters.
    """
    def __init__(self):
        super().__init__(
            username=secrets['email']['username'],
            password=secrets['email']['password'],
            cache_id_file=Path(Path(__file__).parent, 'last_id.json')
        )
        self.clicksend = ClickSend(
            username=secrets['clicksend']['username'],
            api_key=secrets['clicksend']['API_KEY'],
            return_addr=Address(**secrets['production_address']['return'])
        )
        self.riddler = Riddler()

    def handle_new_email(self, new_id, msg):
        response_file = self.riddler.get_response_letter(msg)
        logger.info(f'Sending {response_file} as a response to {msg}')
        with open(response_file, 'rb') as respf:
            response = respf.read()
        sender = self.get_msg_sender(self._get_msg_data(new_id))
        if 'nac' in sender:
            self.clicksend.send(response, Address(**secrets['production_address']['send']))
        else:
            logger.info(
                f'Not sending letter because it was sent by {sender}, not Nick'
            )
