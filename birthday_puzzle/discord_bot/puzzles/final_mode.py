from typing import List
import re
from hashlib import sha256

from .puzzle import Puzzle

def shaify(msg: str) -> List[str]:
    tokens = [i for i in re.split(r'( |,|\.|!|\?)', msg) if i.strip()]
    if not tokens:
        return ['']
    return [sha256(bytes(t, encoding='utf-8')).hexdigest() for t in tokens]

class FinalMode(Puzzle):

    MOM_MSG = '\n'.join(shaify(
        'Wishing you a Happy Birthday Nick! Love mom, dad, and Lola.'
    ))

    HINT_MSG = '\n'.join(shaify(
        'Just run your mom\'s '
        'message through SHA256, then take that 256 bit digest and use it '
        'as the AES key to decrypt the original message. Enjoy!'
    ))

    @ property
    def prompt(self):
        return (
            'Nice job there Nick! You have almost defeated me, but before you '
            'go, I wanted to share a message from your mother. She says you '
            'smell. Besides that, though, I wanted to make sure her message '
            'was safe in transit, so I went ahead and ran each word through '
            'SHA256. Enjoy!\n\n'
        ) + self.MOM_MSG

    def puzzle_response(self, answer: str) -> str:
        return 'If you need a hint, just say so!'

    def check_answer(self, answer: str) -> bool:
         # this puzzle never ends; he has what he needs to proceed.
        return False

    def hint(self) -> str:
        return self.HINT_MSG
