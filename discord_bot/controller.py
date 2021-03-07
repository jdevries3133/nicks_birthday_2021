from typing import Union

from .puzzles import BadMath, BaseMode, AustralianMode
import discord

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

    def next_puzzle(self) -> Union[str, None]:
        """
        Will return None when there are no puzzles remaining.
        """
        if len(self._puzzles) > 1:
            self._puzzles.pop(0)
        else:
            return None
        return self.get_prompt()

    def commands(self):
        """
        This is not used by anything right now...
        """
        return self._puzzles[0].commands
