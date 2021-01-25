from .Puzzle import Puzzle

class TestPing(Puzzle):
    def __init__(self):
        super().__init__('ping')

    def puzzle_response(self, s):
        if s == 'ping':
            return 'pong'

    def check_answer(self, s):
        if s == 'pong':
            return True
        return False