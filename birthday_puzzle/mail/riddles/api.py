from pathlib import Path

from .riddle_one import RiddleOne
from .riddle_two import RiddleTwo
from .riddle_three import RiddleThree

class Riddler:

    def __init__(self):
        self.riddle_classes = [
            RiddleOne(),
            RiddleTwo(),
            RiddleThree()
        ]
        self.cur_riddle = -1

    def get_response_letter(self, message: str) -> Path:
        """
        Return a path to the response letter as a pathlib.Path object.
        """
        msg = self.riddle_classes[self.cur_riddle].get_response_letter(message)
        if msg:
            return msg
        if self.is_complete():
            return self.send_final_msg()
        return self.get_response_letter(message)

    def send_final_msg(self) -> Path:
        return Path(Path(__file__).parent, 'static', 'final.docx')

    def is_complete(self):
        return self.cur_riddle >= len(self.riddle_classes)

