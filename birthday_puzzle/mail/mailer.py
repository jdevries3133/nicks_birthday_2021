"""
Wrapper class for ClickSend API
"""

import json
from base64 import b64encode
from pathlib import Path

import requests

from .riddles import Riddler
from ..email_puzzles.emailer import EmailBot


class Mailer(EmailBot):

    def __init__(self):
        self.ridl = Riddler()


