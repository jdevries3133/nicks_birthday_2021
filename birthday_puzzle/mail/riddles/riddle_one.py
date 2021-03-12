from pathlib import Path
from typing import Union

from .base import SimpleRiddle


class RiddleOne(SimpleRiddle):
    """
    It is a 5 letter word.  If you take away first letter, it is something you
    get from the sun.  If you remove the third letter, you get a word to use
    when pointing.  Remove the fourth letter you get something to drink.  What
    is it?

    Solution: "Wheat"
    """

    def __init__(self):
        super().__init__(stage_id=1)

    @ property
    def CORRECT_ANSWERS(self) -> list:
        return [
            'wheat',
            'wheat.'
        ]
