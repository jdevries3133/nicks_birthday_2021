import unittest
from unittest.mock import MagicMock, patch

from pathlib import Path

from ..emailer import EmailBot

def readbytes(p):
    with open(p, 'rb') as fl:
        return fl.read()


class TestEmailBot(unittest.TestCase):

    def setUp(self):
        self.emailer = EmailBot()

        # setup mocking
        self.emails = [
            readbytes(p)
            for p in
            Path(Path(__file__).parent, 'mock', 'email').iterdir()
            if p.name.endswith('.email')
        ]


    def test_get_newest_message(self):
        id_, eml = self.emailer.get_newest_message()
        self.assertIsInstance(eml, str)
        self.assertIsInstance(id_, bytes)

    def test_get_msg_subject_getter(self):
        id_, msg = self.emailer.get_newest_message()
        self.assertIsInstance(id_, bytes)
        self.assertIsInstance(msg, str)

    def test_reply(self):
        ...
