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

        # doc returned will be switched between based on this dict
        self.times_called_to_paths = {
            1: Path(self.basedir, '3_initial.docx'),
            2: Path(self.basedir, '3.docx'),
            5: Path(self.basedir, '3_hint_0.docx'),
            10: Path(self.basedir, '3_hint_1.docx'),
        }

        # prev response letter is memoized between breakpoints above
        self.respl_memo = self.times_called_to_paths[1]

    def get_response_letter(self, message) -> Union[Path, None]:
        self.times_called += 1
        if self.times_called not in self.times_called_to_paths:
            return self.respl_memo
        self.respl_memo = self.times_called_to_paths[self.times_called]
        return self.respl_memo
