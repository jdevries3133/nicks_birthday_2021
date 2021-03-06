import unittest

from ..controller import Controller

from ..puzzles import BadMath
from ..puzzles.puzzle import Puzzle


class TestController(unittest.TestCase):

    puzzle_sequence = [
        BadMath,
    ]

    def setUp(self):
        self.controller = Controller()

    def _iter_puzzles(self):
        yield self.controller
        for _ in self.controller._puzzles:
            if puzzle := self.controller.next_puzzle():
                yield puzzle

    def test_puzzle_sequence(self):
        """
        Test that puzzles proceed in the correct order on sequential
        calls to Controller.next_puzzle()
        """
        for i, response in enumerate(self._iter_puzzles()):
            self.assertIsInstance(self.controller._puzzles[i], self.puzzle_sequence[i])

    def test_all_puzzles_derived_from_base(self):
        for puzzle in self.controller._puzzles:
            self.assertIsInstance(puzzle, Puzzle)
