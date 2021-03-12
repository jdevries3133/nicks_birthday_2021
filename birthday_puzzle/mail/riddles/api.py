from pathlib import Path

from .riddle_one import RiddleOne
from .riddle_two import RiddleTwo
from .riddle_three import RiddleThree

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
        msg = self.RIDDLE_CLASSES[self.cur_riddle].get_response_letter(message)
        if msg:
            return msg
        if self.is_complete():
            return self.send_final_msg()
        self.cur_riddle += 1
        return self.get_response_letter(message)

    def send_final_msg(self) -> Path:
        return Path(Path(__file__).parent, 'static', 'final.docx')

    def is_complete(self):
        return self.cur_riddle >= len(self.RIDDLE_CLASSES)

