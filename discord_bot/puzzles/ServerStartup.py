from .Puzzle import Puzzle

class ServerStartup(Puzzle):
    def __init__(self, token):
        super().__init__(
            ('Hey Nick Good job finding me! You should have all the information'
            'you need for this puzzle already so I\'m just going to sit back '
            'and relax')
            )
        self.bot_token = token
    def check_answer(self, answer: str) -> bool:
        if answer == 'done':
            return True
        return False
