from unittest import TestCase

from ..base_mode import BaseMode


class TestBaseMode(TestCase):

    def setUp(self):
        self.puzzle = BaseMode()

    def test_solution(self):
        self.assertTrue(self.puzzle.check_answer('Australian Mode'))

    def test_response(self):
        self.assertEqual(
            self.puzzle.puzzle_response(
                'What?'
            ),
                'What? isn\'t gonna get us any closer to Australian Mode my '
                'friend!'
            )
