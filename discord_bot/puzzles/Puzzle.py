from abc import ABC, abstractmethod

class Puzzle(ABC):
    def __init__(self, prompt):
        self.prompt = prompt
        self.commands = []

    def puzzle_response(self, s):
        return None

    @abstractmethod
    def check_answer(self, s):
        """
        This Method checks to see if the puzzle is complete and returns a 
        boolean value
        """