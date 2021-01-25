from abc import ABC, abstractmethod

class Puzzle(ABC):
    def __init__(self, prompt, answer):
        self.answer = answer
        self.prompt =prompt
        self.commands = []

    
    def puzzle_response(self, s):
        return self.prompt if self.answer == s else None
