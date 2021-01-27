import unittest

from ..emailer import EmailBot


class TestEmailBot(unittest.TestCase):
    """
    TODO: improve this test class with mocking and more specific assertions.
    """

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
        for id_, eml in self.emailer.iter_plain_txt_msg():
            self.assertTrue(eml)
            self.assertIsInstance(id_, bytes)
            self.assertIsInstance(eml, str)

    def test_get_newest_message(self):
        id_, eml = self.emailer.get_newest_message()
        self.assertIsInstance(eml, str)
        self.assertIsInstance(id_, bytes)

    def test_get_msg_subject_getter(self):
        for id_, _ in self.emailer.iter_plain_txt_msg():
            print(self.emailer.get_msg_subject(id_))

