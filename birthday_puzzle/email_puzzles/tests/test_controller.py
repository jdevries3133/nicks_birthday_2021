import unittest
from unittest.mock import patch

from ..control import Controller


@ patch('birthday_puzzle.email_puzzles.control.ArbitraryExecutor.execute')
class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_controller__next__(self, _):
        self.assertEqual(self.controller.cur_puzzle, 1)
        self.assertEqual(next(self.controller), 2)
        self.assertEqual(self.controller.cur_puzzle, 2)

    def test_respond_to(self, mock_exec):
        mock_exec.return_value = {'stdout': 'hello', 'stderr': ''}
        self.assertEqual(
            self.controller.respond_to('print("hello")').strip(),
            'hello'
        )

    def test_respond_to_with_stderr(self, mock_exec):
        expect = 'error\nNameError: name \'error\' is not defined'
        mock_exec.return_value = {
            'stdout': '',
            'stderr': expect
        }
        self.assertIn(
            expect,
            self.controller.respond_to('error'),
        )

    def test_base_case_solution(self, mock_exec):
        mock_exec.return_value = {'stdout': 'Hello, world!\n', 'stderr': ''}
        msg = self.controller.respond_to('print("Hello, world!")')
        self.assertEqual(
            msg,
            self.controller.puzzle_solutions['1']['success_response']
        )
        self.assertEqual(self.controller.cur_puzzle, 2)

    def test_stage_3_solution(self, mock_exec):
        mock_exec.return_value = {'stdout': '1325\n', 'stderr': ''}
        self.controller.cur_puzzle = 3
        solution_code = 'import ctypes\nprint(ctypes.c_short(number).value)'
        msg = self.controller.respond_to(solution_code)
        self.assertEqual(
            msg,
            self.controller.puzzle_solutions['3']['success_response']
        )
