from datetime import datetime
import json
from email import message_from_bytes
from email.utils import parsedate_to_datetime
import imaplib
from pathlib import Path

with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
    CREDENTIALS = json.load(jsonf)


class EmailBot:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.imap.login(
            CREDENTIALS.get('username'),
            CREDENTIALS.get('password')
        )
        self.imap.select('inbox')

    def get_newest_message(self):
        last_id = self.imap.search(None, 'ALL')[1][0].split()[-1]
        return message_from_bytes(self._get_msg_data(last_id)).get_payload()[0].get_payload().strip()

    def iter_plain_txt_msg(self):
        """
        Generator that returns the plain text of each message in the mailbox.
        """
        for id_ in self.iter_mailbox_ids():
            data = self._get_msg_data(id_)
            if isinstance(data, bytes):
                yield message_from_bytes(data).get_payload()[0].get_payload().strip()

    def iter_mailbox_ids(self):
        """
        Generator that returns mailbox message ids most recent first
        """
        for id_ in self.imap.search(None, 'ALL')[1][0].split()[::-1]:
            yield id_

    def _get_msg_data(self, id_):
        data = self.imap.fetch(id_, '(RFC822)')[1][0][1]
        if isinstance(data, bytes):
            return data
        return b''
