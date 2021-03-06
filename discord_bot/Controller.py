from typing import Union

from .puzzles import BadMath
import discord

class Controller():
    def __init__(self):
        self._puzzles = [
            BadMath(
                'Why hello there, I have come up with a brand new system of'
                ' mathematics! It features everything you love about old'
                ' math, addition, subtraction, multiplication, and division'
                ' but with a fun twist. Why don\'t you give it a try?'
                ' Write something that gives you 100 in this NEW MATH and,'
                ' I\'ll give you the key to the next step of this challenge.'
                ' Fair warning, my numbers are dogshit, but you should be able'
                ' to figure it out. '
            )
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
        return self._puzzles[0].commands
