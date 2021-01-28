import unittest
from time import sleep

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
        sleep(0.2)
        self.assertEqual(
            self.controller.respond_to('print("hello")'),
            'hello'
        )

    def test_respond_to_with_stderr(self):
        self.assertIn(
            'error\nNameError: name \'error\' is not defined',
            self.controller.respond_to('error'),
        )

    def test_base_case_solution(self):
        response = self.controller.respond_to('print("Hello, world!")')
        self.assertEqual(response, self.controller.puzzle_solutions['1']['success_response'])
        self.assertEqual(self.controller.cur_puzzle, 2)

    def test_stage_4_solution(self):
        self.controller.cur_puzzle = 4
        solution_code = 'import ctypes\nprint(ctypes.c_short(number).value)'
        response = self.controller.respond_to(solution_code)
        self.assertEqual(
            response,
            self.controller.puzzle_solutions['4']['success_response']
        )

