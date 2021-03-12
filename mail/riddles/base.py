from abc import ABC, abstractmethod
from typing import Union
from pathlib import Path

class RiddleBase(ABC):

    BASE_DIR = Path(Path(__file__).parent, 'static')

    def __init__(self):
        self.times_called = 0

    @ abstractmethod
    def get_response_letter(self, message: str) -> Union[Path, None]:
        """
        Return path to the response doc or None if the puzzle is solved.
        """
        ...

class SimpleRiddle(RiddleBase):
    """
    Stage 1 and 2 are simple riddles. They just have two message types:

    - Initial
    - Normal

    The initial message transitions from the previous puzzle, and normal
    messages are sent thereafter.
    """

    def __init__(self, stage_id: int):
        self.stage_id = stage_id
        super().__init__()

    def get_response_letter(self, message: str) -> Union[Path, None]:
        self.times_called += 1
        if self.times_called == 1:
            return Path(
                self.BASE_DIR,
                str(self.stage_id),
                f'{self.stage_id}_initial.docx'
            )
        return Path(
                self.BASE_DIR,
                str(self.stage_id),
                f'{self.stage_id}.docx'
            )
