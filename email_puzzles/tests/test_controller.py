import unittest

from ..control import Controller
from ..executor import ArbitraryExecutor

class TestController(unittest.TestCase):

    # must use same executor instance throughout to protect from rate
    # limiting.
    executor = ArbitraryExecutor()

    def setUp(self):
        self.controller = Controller()
        self.controller.executor = self.executor

    def test_controller__next__(self):
        self.assertEqual(self.controller.cur_puzzle, 1)
        self.assertEqual(next(self.controller), 2)
        self.assertEqual(self.controller.cur_puzzle, 2)

    def test_respond_to(self):
        self.assertEqual(
            self.controller.respond_to('print("hello")'),
            'hello'
        )

    def test_respond_to_with_stderr(self):
        self.assertEqual(
            self.controller.respond_to('error'),
            '\nTraceback (most recent call last):\n  File "code.code", line '
            '254, in <module>\n    error\nNameError: name \'error\' is not '
            'defined'
        )
