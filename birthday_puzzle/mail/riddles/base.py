from abc import ABC, abstractmethod
from typing import Union
from pathlib import Path

class RiddleBase(ABC):

    BASE_DIR = Path(Path(__file__).parent, 'static')

    def __init__(self):
        self.times_called = 0

    def is_solved(self, message) -> bool:
        for a in self.CORRECT_ANSWERS:  # type: ignore
            if a in message:
                return True
        return False

    def respond(self, message) -> Union[Path, None]:
        """
        Return path to the response doc or None if the puzzle is solved.
        """
        self.times_called += 1
        for answer in self.CORRECT_ANSWERS:  # type: ignore
            if answer in message.lower().strip():
                return None
        return self.get_response_letter()

    @ abstractmethod
    def get_response_letter(self) -> Path:
        """
        Return the letter that should be sent.
        """

    @ property
    @ abstractmethod
    def CORRECT_ANSWERS(self) -> list:
        ...

class SimpleRiddle(RiddleBase):
    """
    Stage 1 and 2 are simple riddles. They just have two message types:

    - Initial
    - Normal

    The initial message transitions from the previous puzzle, and normal
    messages are sent thereafter.

    By using a strict file naming convention, this class can handle both
    puzzles.
    """

    def __init__(self, stage_id: int):
        self.stage_id = stage_id
        super().__init__()

    def get_response_letter(self, message: str) -> Path:
        if self.times_called == 1:
            return Path(
                self.BASE_DIR,
                str(self.stage_id),
                f'{self.stage_id}_initial.pdf'
            )
        return Path(
                self.BASE_DIR,
                str(self.stage_id),
                f'{self.stage_id}.pdf'
            )
