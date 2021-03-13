from pathlib import Path
from typing import Union

from .base import RiddleBase


class RiddleThree(RiddleBase):
    """
    One day, Nick decides that he's hungry for a snack. He collects the
    following ingredients:

    1. All-purpose flour
    2. Baking powder
    3. Granulated sugar
    4. Salt
    5. Unsalted butter
    6. Buttermilk

    After mixing, cutting and baking at 425 F for 12 minutes, he is left with
    6 servings of a wonderful baked good.

    What is it?

    HINT -- The butter is very cold.

    HINT TWO -- The dough is laminated.

    Solution:
    Biscuit
    """

    def __init__(self):
        super().__init__()
        self.basedir = Path(self.BASE_DIR, '3')

        self.times_called_to_paths = {
            1: Path(self.basedir, '3_initial.pdf'),
            2: Path(self.basedir, '3.docx'),
            5: Path(self.basedir, '3_hint_0.pdf'),
            10: Path(self.basedir, '3_hint_1.pdf'),
        }

        # memoized response
        self.response_letter_memo = self.times_called_to_paths[1]

    def get_response_letter(self, message) -> Path:

        # return last returned if cur num calls is not in above dict
        if self.times_called not in self.times_called_to_paths:
            return self.response_letter_memo

        # otherwise, memoize and return new letter
        self.response_letter_memo = (
            self.times_called_to_paths[self.times_called]
        )
        return self.response_letter_memo

    @ property
    def CORRECT_ANSWERS(self) -> list:
        return ['biscuit']
