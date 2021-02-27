import unittest

from ..Controller import Controller

from ..puzzles import BadMath, ChessPuzzle
from ..puzzles.Puzzle import Puzzle


class TestController(unittest.TestCase):

    puzzle_sequence = [
        BadMath,
        ChessPuzzle,
    ]

    def setUp(self):
        self.controller = Controller()

    def _iter_puzzles(self):
        yield self.controller
        for _ in self.controller._puzzles:
            yield self.controller.next_puzzle()

    def test_puzzle_sequence(self):
        """
        Test that puzzles proceed in the correct order on sequential
        calls to Controller.next_puzzle()
        """
        for i, response in enumerate(self._iter_puzzles()):
            self.assertIsInstance(self.controller._puzzles[0], self.puzzle_sequence[i])

    def test_all_puzzles_derived_from_base(self):
        for puzzle in self.controller._puzzles:
            self.assertIsInstance(puzzle, Puzzle)
