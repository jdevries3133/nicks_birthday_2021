from unittest import TestCase

from ..dark_mode import DarkMode

class TestDarkMode(TestCase):

    def setUp(self):
        self.dm = DarkMode()

    def test_response(self):
        res = self.dm.puzzle_response('hi')
        self.assertEqual(
            DarkMode.ROTATED_BRAILLE_MESSAGE,
            res
        )

    def test_solution(self):
        self.assertTrue(
            self.dm.check_answer('tisket a biscuit the baker has a dog')
        )
