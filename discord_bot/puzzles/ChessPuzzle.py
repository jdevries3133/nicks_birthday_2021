from .Puzzle import Puzzle

class ChessPuzzle(Puzzle):
    def __init__(self):
        super().__init__('Help me out with this CHESS URL HERE')

    def check_answer(self, s):
    	return True

    #TODO:finish puzzle