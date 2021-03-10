"""
A docx file must be uploaded to send the letter, so it will be generated
here.
"""

from pathlib import Path

from docx import Document as docx_mkdoc
from docx.document import Document

from .riddles import RIDDLE_CLASSES

BASE_DIR = Path(__file__).parent


class LetterController:
    def __init__(self):
        self._doc = docx_mkdoc()
        self._cur_puzzle = 0
        self.message = ''

    def respond_to(self, message: str) -> bytes:
        """
        Return a word document in bytes.
        """
        # TODO: figure out how to save into byte buffer instead of using temp
        # file
        self.message = message
        self.doc.save(Path(BASE_DIR, 'temp.docx'))
        with open('temp.docx', 'rb') as docf:
            data = docf.read()
        return data

    @ property
    def doc(self) -> Document:
        ...

    @ doc.getter
    def doc(self) -> Document:
        # TODO: set self._doc to the doc from the current puzzle
        self._cur_puzzle += 1
        return self._doc
