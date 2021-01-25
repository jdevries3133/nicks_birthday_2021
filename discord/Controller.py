import puzzles

class Controller():
    def __init__(self):
        self._puzzles = [
            puzzles.TestPing()
            #puzzles.ServerSetup('uhu', 'hint', 'answer'),
            #puzzles.ChessPuzzle('yep', 'hint', 'answer'),
        ]

    def get_response(self, s):
        if(s == self._puzzles[0].answer):
            return self.next_puzzle()
        return self._puzzles[0].puzzle_response()

    def get_prompt(self):
        return self._puzzles[0].prompt

    def next_puzzle(self):
        if(len(self._puzzles) > 1):
            self._puzzles.pop(0)
        return self.get_prompt()
