import re
from typing import Iterator
import json
from email import message_from_bytes
import imaplib
from time import sleep
from pathlib import Path

from .control import Controller

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

    def listen(self):
        """
        Listen for and respond to emails by using the controller.
        """
        while True:
            found = False
            for id_, msg in self.iter_plain_txt_msg(criteria='NEW'):
                found = True
                self.reply(
                    id_,
                    self.controller.respond_to(msg)
                )
            if found:
                print('found something')
            else:
                print('found nothing')
            found = False
            sleep(1)

    def reply(self, id_, msg):
        print(f'replying to id_ {id_} with message {msg}')
        ...

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
    def get_msg_subject(self, id_) -> str:
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

    def iter_plain_txt_msg(self, criteria='ALL') -> Iterator[tuple]:
        """
        Generator that returns a tuple of the id and the plain text of each
        message in the mailbox.
        """
        for id_ in self.iter_mailbox_ids(criteria=criteria):
            data = self._get_msg_data(id_)
            if isinstance(data, bytes):
                yield id_, message_from_bytes(data).get_payload()[0].get_payload().strip()

    @ refresh
    def iter_mailbox_ids(self, criteria='ALL') -> Iterator[bytes]:
        """
        Generator that returns mailbox message ids most recent first
        """
        print(criteria)
        for id_ in self.imap.search(None, criteria)[1][0].split()[::-1]:
            yield id_

    @ refresh
    def _get_msg_data(self, id_) -> bytes:
        data = self.imap.fetch(id_, '(RFC822)')[1][0][1]
        if isinstance(data, bytes):
            return data
        return b''
