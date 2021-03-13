import logging
from pathlib import Path

from .riddle_one import RiddleOne
from .riddle_two import RiddleTwo
from .riddle_three import RiddleThree

logger = logging.getLogger(__name__)

class Riddler:

    RIDDLE_CLASSES = [
        RiddleOne(),
        RiddleTwo(),
        RiddleThree()
    ]

    def __init__(self):
        self.cur_riddle = 0

    def get_response_letter(self, message: str) -> Path:
        """
        Return a path to the response letter as a pathlib.Path object.
        """
        letter = self.RIDDLE_CLASSES[self.cur_riddle].get_response_letter(message)
        logger.debug(f'Responding to message {message} with letter {letter}')
        if letter:
            return letter
        if self.is_complete():
            return self.send_final_msg()
        self.cur_riddle += 1
        return self.get_response_letter(message)

    def send_final_msg(self) -> Path:
        return Path(Path(__file__).parent, 'static', 'final.pdf')

    def is_complete(self):
        return self.cur_riddle >= len(self.RIDDLE_CLASSES)

