import unittest

from ..emailer import EmailBot


class TestEmailBot(unittest.TestCase):

    def setUp(self):
        self.emailer = EmailBot()

    def test_iter_mailbox(self):
        last_id = None
        for id_ in self.emailer.iter_mailbox_ids():
            if last_id:
                self.assertLess(int(id_), int(last_id))
            last_id = id_
        self.assertTrue(self.emailer)

    def test_email_parse(self):
        for eml in self.emailer.iter_plain_txt_msg():
            self.assertTrue(eml)
            self.assertIsInstance(eml, str)

    def test_get_newest_message(self):
        eml = self.emailer.get_newest_message()
        self.assertIsInstance(eml, str)
