from unittest import TestCase

from ..api import Riddler



def for_every_puzzle(func):
    def wrap(*a, **kw):
        while not a[0].rid.is_complete():
            for _ in range(20):
                response_f = a[0].rid.get_response_letter('')
                if not response_f.exists():
                    raise Exception(f'Response file {response_f} does not exist')
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
    def test_all_are_docx(self, response_f):
        self.assertTrue(
            response_f.name.endswith('.pdf') or response_f.name.endswith('.docx')
        )

    def test_final_msg_ready(self):
        msg = self.rid.send_final_msg()
        self.assertTrue(msg.exists())

    def test_complete_solution(self):
        for _ in range(len(self.rid.RIDDLE_CLASSES)):
            answer = (
                self.rid.RIDDLE_CLASSES[self.rid.cur_riddle].CORRECT_ANSWERS[0]
            )
            self.rid.get_response_letter(answer)


def every_riddle_class(func):
    def wrap(*a, **kw):
        for cls in Riddler.RIDDLE_CLASSES:
            func(a[0], cls)
    return wrap

class TestRiddleClasses(TestCase):

    @ every_riddle_class
    def test_answers_are_lowercase(self, riddle_cls):
        """
        Messages are made all lowercase for comparison, so all answers
        should be too.
        """
        for a in riddle_cls.CORRECT_ANSWERS:
            for char in a:
                self.assertFalse(char.isupper())

