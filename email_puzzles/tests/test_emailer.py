"""
DO NOT ADD TO THIS TEST SUITE.

I did not do mocking correctly here. It passes, but it might not continue to
pass. Honestly, if it starts failing, it might be just as well to delete it
or at least to significantly simplify the assertions which will at least keep
the code being run.

Because mocking is wrong, the test suite goes out to the network every time,
so it's ultimately dependent on what is in the email inbox and ultimately
just gets very gnarly.
"""
from typing import NamedTuple, Iterator, Type
from email import message_from_bytes
import unittest
from unittest.mock import patch, MagicMock

from pathlib import Path

from ..emailer import EmailBot

class TestEmailBot(unittest.TestCase):

    def setUp(self):
        self.emailer = EmailBot()

    @ staticmethod
    def _mock_email(email_id: int):
        with open(
            Path(Path(__file__).parent, 'mock', 'email', f'{email_id}.email'),
            'rb'
        ) as emlf:
            return (
                '',
                (
                    (
                        '',
                        emlf.read(),
                    ),
                ),
            )

    @ patch('imaplib.IMAP4_SSL')
    def get_mock(self, imap_mock) -> Iterator[NamedTuple]:

        class MockItem(NamedTuple):
            expected_id: bytes
            expected_eml: str
            mock: MagicMock

        for i in range(9, -1, -1):
            eml_data = self._mock_email(i)
            imap_mock.fetch.return_value = eml_data
            if not i % 3:
                imap_mock.search.return_value = (
                    'OK',
                    [b'1 2 3 4 5 6 7 8 9 10 11 12']
                )
                expected_id = b'12'
            elif i % 3 == 1:
                imap_mock.search.return_value = (
                    'OK',
                    [b'1 2 3 4 8 9 10 11 12']
                )
                expected_id = b'12'
            else:
                imap_mock.search.return_value = ('OK', [b'1 2 3 7 8 9'])
                expected_id = b'9'

            yield MockItem(
                expected_id=expected_id,
                expected_eml=message_from_bytes(
                    eml_data[1][0][1]
                ).get_payload()[0].get_payload().strip(),
                mock=imap_mock
            )

    def test_get_newest_message(self):
        for expect_id, expect_eml, mockcls in self.get_mock():  # type: ignore
            self.emailer.imap = mockcls
            id_, eml = self.emailer.get_newest_message()
            self.assertEqual(id_, expect_id)
            self.assertEqual(eml, expect_eml)

    def test_get_msg_subject(self):
        subjects = [
            'hi',
            'hejkrla',
            'test',
            'hey there!',
            'Fwd: hi',
            'Simple Plain Email',
            'App password created',
            '2-Step Verification turned on',
            'Critical security alert',
            'Dev, finish setting up your new Google Account',
        ]
        for i, mockdata in enumerate(self.get_mock()):  # type: ignore
            expect_id, expect_eml, mockcls = mockdata
            self.emailer.imap = mockcls
            subject = self.emailer.get_msg_subject(
                self.emailer._get_msg_data(expect_id)
            )
            self.assertEqual(subject, subjects[i])

    def test_get_msg_sender(self):
        senders = [
            'jdevries3133@gmail.com',
            'jdevries3133@gmail.com',
            'jdevries3133@gmail.com',
            'jdevries3133@gmail.com',
            'jdevries3133@gmail.com',
            'jdevries3133@gmail.com',
            'no-reply@accounts.google.com',
            'no-reply@accounts.google.com',
            'no-reply@accounts.google.com',
            'googlecommunityteam-noreply@google.com',
        ]
        for i, mockdata in enumerate(self.get_mock()):
            expect_id, expect_eml, mockcls = mockdata
            self.emailer.imap = mockcls
            sender = (
                self.emailer.get_msg_sender(
                    self.emailer._get_msg_data(expect_id)
                )
            )
            self.assertEqual(sender, senders[i])

    @ patch('smtplib.SMTP_SSL')
    def test_reply(self, smtp_mock):
        smtp_mock.sendmail.return_value = None
        self.emailer.smtp.connection = smtp_mock
        expect_id, _, mockcls = next(self.get_mock())
        self.emailer.imap = mockcls
        self.emailer.reply(expect_id, 'Hello!')
        self.assertEqual(
            'login',
            smtp_mock.mock_calls[1][0][3:]
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][0][3:],
            'sendmail'
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][1][0],
            'jdevries3133@gmail.com'
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][1][1],
            'jkdlasjkfl4jkl@gmail.com'
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][1][2],
            (
                'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: '
                '1.0\nContent-Transfer-Encoding: 7bit\nSubject: hi\n'
                'From: jkdlasjkfl4jkl@gmail.com\n'
                'To: jdevries3133@gmail.com\n\n'
                'Hello!'
            )
        )
        smtp_mock.reset_mock()
