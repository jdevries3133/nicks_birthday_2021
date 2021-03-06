from .Puzzle import Puzzle

class PingTest(Puzzle):
    def __init__(self):
        super().__init__('ping')

    def puzzle_response(self, s):
        if s == 'ping':
            return 'pong'

    def check_answer(self, answer: str) -> bool:
        if answer == 'pong':
            return True
        return False
