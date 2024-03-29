from abc import ABC, abstractmethod

class Puzzle(ABC):
    def __init__(self):
        self.commands = []

    @ property
    @ abstractmethod
    def prompt(self) -> str:
        """
        First message that is sent.
        """

    @ abstractmethod
    def puzzle_response(self, answer: str) -> str:
        """
        Return the response to a given answer if the puzzle is not solved yet.
        """

    @ abstractmethod
    def check_answer(self, answer: str) -> bool:
        """
        This Method checks to see if the puzzle is complete and returns a
        boolean value
        """

    def hint(self) -> str:
        return self.prompt
