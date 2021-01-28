from .puzzles import ServerStartup, ChessPuzzle
import discord

class Controller():
    def __init__(self):
        self._puzzles = [
            ServerStartup('TODO'),
            ChessPuzzle(),
        ]

    def get_response(self, s):
        if(self._puzzles[0].check_answer(s)):
            return self.next_puzzle()
        return self._puzzles[0].puzzle_response(s)

    def get_prompt(self):
        return self._puzzles[0].prompt

    def next_puzzle(self):
        if(len(self._puzzles) > 1):
            self._puzzles.pop(0)
        return self.get_prompt()

    def commands(self):
        return self._puzzles[0].commands
