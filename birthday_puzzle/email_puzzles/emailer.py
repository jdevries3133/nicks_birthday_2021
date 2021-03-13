import re
from typing import NamedTuple, Union
import json
import ssl
import os
from email import message_from_bytes
from email.message import EmailMessage
import imaplib
import logging
from time import sleep
import smtplib
from pathlib import Path
from unittest.mock import MagicMock

from .control import Controller

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent

with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
    CREDENTIALS = json.load(jsonf)

class EmailSender:
    """
    Use smtplib to send emails. A smtp connection must be managed and
    instantiated separately from the imap connection in the class below.
    """
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
        logger.debug(f'sending email from {self.username} to {to}')
        if self.username in to:
            logger.info('Skipping email to myself to prevent a loop')
            return
        msg = EmailMessage()
        msg.set_content(msg_text)
        msg['Subject'] = subject
        msg['From'] = from_
        msg['To'] = to
        self.connection.sendmail(from_, to, msg.as_string())
        logger.info(f'Sent message to {to} as {from_} with subject, "{subject}"')
        logger.debug(f'Message text: {msg_text}')

def refresh(func):
    """
    Refresh the email inbox before running this method.
    """
    def wrapper(*args, **kw):
        args[0].imap.select('inbox')
        return func(*args, **kw)
    return wrapper


###############################################################################

        ## Types for the EmailBot ##

class NewestMessage(NamedTuple):
    last_id: bytes
    message: str

class MsgDetail(NamedTuple):
    subject: str
    sender: str

###############################################################################

class EmailBot:
    """
    Use imaplib to poll for new emails and ask the controller for a response
    if needed.
    """


    def __init__(self, username: str=None, password: str=None, cache_id_file: Path=None):
        self.username = username if username else CREDENTIALS.get('username')
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.imap.login(
            self.username,
            password if password else CREDENTIALS.get('password')
        )
        self.smtp = EmailSender(
            self.username,
            password if password else CREDENTIALS.get('password')
        )
        self.controller = Controller()
        self.imap.select('inbox')
        self._last_id_cache_file = (
            cache_id_file if cache_id_file else Path(BASE_DIR, 'last_id.json')
        )
        if os.path.exists(self._last_id_cache_file):
            with open(self._last_id_cache_file, 'r') as cachef:
                self._last_id = bytes(json.load(cachef)['lastId'], 'utf-8')
        else:
            self._last_id = b'0'

        self.WAIT = 10  # email polling interval
        logger.debug(f'initialized with last_id {self._last_id}')

    def __setattr__(self, name, value, *, init=False):
        if name == '_last_id' and not init:
            with open(self._last_id_cache_file, 'w') as jsonf:
                json.dump({'lastId': str(value, 'utf-8')}, jsonf)
            self.__dict__['_last_id'] = value
            return
        return super().__setattr__(name, value)

    def listen(self):
        """
        Listen for and respond to emails by using the controller.
        """
        while True:
            sleep(self.WAIT)
            new_id, msg = self.get_newest_message()
            if new_id != self._last_id:
                self.handle_new_email(new_id, msg)

    def handle_new_email(self, new_id, msg):
        self._print_msg_recieved(new_id)
        self.reply(
            new_id,
            self.controller.respond_to(msg)
        )
        self._last_id = new_id

    def reply(self, id_: bytes, msg: str):
        data = self._get_msg_data(id_)
        with self.smtp as send:
            send.email(
                to=self.get_msg_sender(data),
                from_=f'{self.username}@gmail.com',
                subject=f'Re: {self.get_msg_subject(data)}',
                msg_text=msg
            )
        logger.info(f'replying to id {id_} with message {msg}')

    @ refresh
    def get_newest_message(self) -> NewestMessage:
        """
        Returns tuple of the id and message text as a string.
        """
        last_id = self.imap.search(None, 'ALL')[1][0].split()[-1]
        msg = message_from_bytes(
            self._get_msg_data(
                last_id
            )
        ).get_payload()
        if isinstance(msg, str):
            return NewestMessage(last_id, msg)
        return NewestMessage(last_id, msg[0].get_payload().strip())

    def get_msg_detail(self, id_: bytes) -> MsgDetail:
        msg = self._get_msg_data(id_)
        return MsgDetail(
            subject=self.get_msg_subject(msg),
            sender=self.get_msg_sender(msg)
        )

    def get_msg_subject(self, data: bytes) -> str:
        """
        Parse the subject from a message.
        """
        match = self._email_regsearch(
            data=data,
            pattern=r'^Subject: (.*)$',
            mo_num=1
        )
        if not match:
            logger.error('Email subject not found')
            return ''
        return match

    def get_msg_sender(self, data: bytes) -> str:
        """
        Parse the sender from a message.
        """
        sender =  self._email_regsearch(
            data=data,
            pattern=r'From: (.*)',
            mo_num=1
        )
        if not sender:
            logger.error('Email sender not found')
            return ''
        if '<' in sender and '>' in sender:
            return re.search('<(.*)>', sender)[1]
        logger.debug(f'message sender was {sender}')
        return sender

    @ refresh
    def _get_msg_data(self, id_) -> bytes:
        data = self.imap.fetch(id_, '(RFC822)')[1][0][1]
        if isinstance(data, bytes):
            return data
        return b''

    @ staticmethod
    def _email_regsearch(*, data: bytes, pattern: str, mo_num: int) -> Union[str, None]:
        pattern_ = re.compile(pattern)
        try:
            lines = str(data, encoding='utf-8').split('\n')
        except TypeError:
            return None
        for l in lines:
            l = l.strip()
            if mo := re.search(pattern_, l):
                return mo[mo_num]


    @ staticmethod
    def _print_msg_recieved(new_id: bytes) -> None:
        logger.info(
            ('*' * 30)
            + f' NEW MESSAGE RECIEVED (id: {new_id})'
            + ('*' * 30)
        )
