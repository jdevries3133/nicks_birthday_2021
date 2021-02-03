import re
from typing import NamedTuple
import json
import ssl
from email import message_from_bytes
from email.mime.text import MIMEText
import imaplib
import logging
from time import sleep
import smtplib
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

class EmailSender:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        context = ssl.create_default_context()
        self.connection = smtplib.SMTP_SSL(
            'smtp.gmail.com',
            port=465,
            context=context,
        )
        self.connection.login(
            self.username,
            self.password,
        )
        return self

    def __exit__(self, *_):
        self.connection.close()

    def email(self, *, to: str, from_:str, subject: str, msg_text: str) -> None:
        msg = MIMEText(msg_text)
        msg['Subject'] = subject
        msg['From'] = from_
        msg['To'] = to
        self.connection.sendmail(to, from_, msg.as_string())


class EmailBot:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.username = CREDENTIALS.get('username')
        self.imap.login(
            self.username,
            CREDENTIALS.get('password')
        )
        self.smtp = EmailSender(
            self.username,
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
        data = self._get_msg_data(id_)
        with self.smtp as send:
            send.email(
                to=self.get_msg_sender(data),
                from_=f'{self.username}@gmail.com',
                subject=self.get_msg_subject(data),
                msg_text=msg
            )
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

    def get_msg_detail(self, id_: bytes) -> NamedTuple:
        class MsgDetail(NamedTuple):
            subject: str
            sender: str
        msg = self._get_msg_data(id_)
        return MsgDetail(
            subject=self.get_msg_subject(msg),
            sender=self.get_msg_sender(msg)
        )

    def get_msg_subject(self, data: bytes) -> str:
        """
        Parse the subject from a message.
        """
        return self._email_regsearch(
            data=data,
            pattern=r'^Subject: (.*)$',
            mo_num=1
        )

    def get_msg_sender(self, data: bytes) -> str:
        """
        Parse the sender from a message.
        """
        return self._email_regsearch(
            data=data,
            pattern=r'From: (.*)<(.*)>',
            mo_num=2
        )

    @ staticmethod
    def _email_regsearch(*, data: bytes, pattern: str, mo_num: int) -> str:
        pattern_ = re.compile(pattern)
        for l in str(data, encoding='utf-8').split('\n'):
            l = l.strip()
            if (mo := re.search(pattern_, l)):
                return mo[mo_num]
        raise Exception(f'No match for {pattern}')

    @ refresh
    def _get_msg_data(self, id_) -> bytes:
        data = self.imap.fetch(id_, '(RFC822)')[1][0][1]
        if isinstance(data, bytes):
            return data
        return b''
