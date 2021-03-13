"""
Wrapper class for ClickSend API
"""

import json
from base64 import b64encode
from pathlib import Path

import requests

from .clicksend import ClickSend
from .riddles import Riddler
from ..email_puzzles.emailer import EmailBot

with open(Path(__file__).parent, 'secrets.json') as jsonf:
    secrets = json.load(jsonf)

class Mailer(EmailBot):
    def __init__(self):
        self.clicksend = ClickSend(
            username=secrets['clicksend']['username'],
            api_key=secrets['clicksend']['API_KEY']
        )
