"""
Base mode for the first of the encryption tests.
"""

from .puzzle import Puzzle


class BaseMode(Puzzle):
    def __init__(self):
        super().__init__()
        self.prompt = (
            'Wow! Nice job with that last one. I hope it wasn\'t too easy. '
            'Just shoot me an email at [[encryption digest]] to take this '
            'conversation to the next level!\n\nWait, hold on a sec... '
            'something isn\'t right there. Try entering `Australian Mode` to '
            'see if we can straighten this out.'
        )

    def puzzle_response(self, answer: str) -> str:
        return (
            f'{answer} isn\'t gonna get us any closer to Australian Mode '
            'my friend!'
        )

    def check_answer(self, answer: str) -> bool:
        return answer == 'Australian Mode'
