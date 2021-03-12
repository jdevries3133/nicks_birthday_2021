from unittest import TestCase
from ..api import Riddler


def for_every_puzzle(func):
    def wrap(*a, **kw):
        while not a[0].rid.is_complete():
            for _ in range(20):
                response_f = a[0].rid.get_response_letter('')
                func(a[0], response_f)
            a[0].rid.cur_riddle += 1
    return wrap

class TestRiddler(TestCase):

    def setUp(self):
        self.rid = Riddler()

    @ for_every_puzzle
    def test_all_paths_exist(self, response_f):
        self.assertTrue(response_f.exists())

    @ for_every_puzzle
    def test_all_docx(self, response_f):
        self.assertTrue(response_f.name.endswith('.docx'))

    def test_final_msg_ready(self):
        msg = self.rid.send_final_msg()
        self.assertTrue(msg.exists())
