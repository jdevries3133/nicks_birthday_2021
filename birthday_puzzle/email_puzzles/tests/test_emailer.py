import json
from io import StringIO
from typing import NamedTuple, Iterator
from email import message_from_bytes
import unittest
from unittest.mock import patch, MagicMock, mock_open

from pathlib import Path

from ..emailer import EmailBot

@ patch('birthday_puzzle.email_puzzles.emailer.open', mock_open(read_data=json.dumps({
    'lastId': '13'
})))
class TestEmailBot(unittest.TestCase):

    @ patch('birthday_puzzle.email_puzzles.emailer.open', mock_open(read_data=json.dumps({
        'lastId': '13'
    })))
    @ patch('birthday_puzzle.email_puzzles.emailer.imaplib')
    @ patch('birthday_puzzle.email_puzzles.emailer.smtplib')
    def setUp(self, imap_mock, smtp_mock):
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

    @ patch('birthday_puzzle.email_puzzles.emailer.smtplib')
    def test_reply(self, smtp_mock):
        # smtp_mock.sendmail.return_value = None
        expect_id, _, mockcls = next(self.get_mock())
        self.emailer.imap = mockcls
        self.emailer.reply(expect_id, 'Hello!')
        self.assertEqual(
            'SMTP_SSL().login',
            smtp_mock.mock_calls[1][0]
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][0],
            'SMTP_SSL().sendmail'
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][1][0],
            'jkdlasjkfl4jkl@gmail.com'
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][1][1],
            'jdevries3133@gmail.com'
        )
        self.assertEqual(
            smtp_mock.mock_calls[2][1][2],
            'Content-Type: text/plain; charset="utf-8"\n'
            'Content-Transfer-Encoding: 7bit\n'
            'MIME-Version: 1.0\n'
            'Subject: Re: hi\n'
            'From: jkdlasjkfl4jkl@gmail.com\n'
            'To: jdevries3133@gmail.com\n\n'
            'Hello!\n'
        )
        smtp_mock.reset_mock()

    @ patch('birthday_puzzle.email_puzzles.emailer.os.path.exists', return_value=True)
    def test_last_id_cache_read(self, *_):
        with patch(
            'birthday_puzzle.email_puzzles.emailer.open',
            mock_open(read_data=json.dumps(
                {
                    'lastId': '11'
                }),
            )
        ) as mock_file:
            emailer = EmailBot()
            self.assertEqual(emailer._last_id, b'11')

    def test_last_id_cache_written_on_setattr(self):
        with patch(
            'birthday_puzzle.email_puzzles.emailer.open',
            mock_open(read_data=json.dumps(
                {
                    'lastId': '13'
                })
            )
        ) as mock_file:
            emailer = EmailBot()
            mock_file.reset_mock()
            emailer._last_id = b'13'
            handle = mock_file()
            expected_calls = ['{', '"lastId"', ': ', '"13"', '}']
            for expect, actual in zip(expected_calls, handle.write.mock_calls):
                self.assertEqual(
                    expect,
                    actual[1][0]
                )
