import discord

from .puzzles import BadMath, BaseMode, AustralianMode

class ControllerPuzzlesEmptyException(Exception):
    ...

class Controller():
    def __init__(self):
        self._puzzles = [
            BadMath(),
            BaseMode(),
            AustralianMode()
        ]

    def get_response(self, s):
        if self._puzzles[0].check_answer(s):
            return self.next_puzzle()
        return self._puzzles[0].puzzle_response(s)

    def get_prompt(self):
        return self._puzzles[0].prompt

    def get_hint(self):
        return self._puzzles[0].hint()

    def next_puzzle(self) -> str:
        """
        Will return None when there are no puzzles remaining.
        """
        if len(self._puzzles) > 1:
            self._puzzles.pop(0)
        else:
            raise ControllerPuzzlesEmptyException(
                "The final puzzle has been popped from the controller and "
                "the controller currently has no more puzzles. This should "
                "not happen. The final puzzle should never end, and should "
                "repeat the final discord puzzle departure message forever."
            )
        return self.get_prompt()

    def commands(self):
        """
        This is not used by anything right now...
        """
        return self._puzzles[0].commands
