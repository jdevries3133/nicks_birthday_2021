import re
import json
from email import message_from_bytes
import imaplib
import logging
from time import sleep
from pathlib import Path

from .control import Controller

logger = logging.getLogger(__name__)

with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
    CREDENTIALS = json.load(jsonf)


def refresh(func):
    def wrapper(*args, **kw):
        args[0].imap.select('inbox')
        return func(*args, **kw)
    return wrapper

class EmailBot:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.imap.login(
            CREDENTIALS.get('username'),
            CREDENTIALS.get('password')
        )
        self.controller = Controller()
        self.imap.select('inbox')
        self._last_id = b''

    def listen(self):
        """
        Listen for and respond to emails by using the controller.
        """
        while True:
            new_id, msg = self.get_newest_message()
            if new_id != self._last_id:
                self.reply(
                    new_id,
                    self.controller.respond_to(msg)
                )
                self._last_id = new_id
            sleep(10)

    def reply(self, id_: bytes, msg: str):
        logger.info(f'replying to id_ {id_} with message {msg}')

    @ refresh
    def get_newest_message(self) -> tuple:
        """
        Returns tuple of the id and message text as a string.
        """
        return (
            last_id := self.imap.search(None, 'ALL')[1][0].split()[-1],
            message_from_bytes(
                self._get_msg_data(
                    last_id
                )
            ).get_payload()[0].get_payload().strip()
        )

    @ refresh
    def get_msg_subject(self, id_: bytes) -> str:
        """
        Get the subject of a message for a given id.
        """
        data = self._get_msg_data(id_)
        pattern = re.compile(r'^Subject: (.*)$')
        for l in str(data, encoding='ascii').split('\n'):
            l = l.strip()
            if (mo := re.search(pattern, l)):
                return mo[1]
        raise Exception('Email subject not found')

    @ refresh
    def _get_msg_data(self, id_) -> bytes:
        data = self.imap.fetch(id_, '(RFC822)')[1][0][1]
        if isinstance(data, bytes):
            return data
        return b''
