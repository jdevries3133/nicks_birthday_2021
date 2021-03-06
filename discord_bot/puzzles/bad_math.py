from enum import Enum
import logging
import re

from .puzzle import Puzzle

logger = logging.getLogger(__name__)

class BadMath(Puzzle):

    def __init__(self):
        super().__init__()
        self.prompt = (
            'Why hello there, I have come up with a brand new system of'
            ' mathematics! It features everything you love about old'
            ' math, addition, subtraction, multiplication, and division'
            ' but with a fun twist. Why don\'t you give it a try?'
            ' Write something that gives you 100 in this NEW MATH and,'
            ' I\'ll give you the key to the next step of this challenge.'
            ' Fair warning, my numbers are dogshit, but you should be able'
            ' to figure it out. '
        )

    def check_answer(self, answer: str) -> bool:
        """
        WARNING: this one takes s as a string
        """
        # in our number system
        one_hundred = 'dogshittrashgarbagetrashdogshit'
        return self.eval_stmt(answer) == one_hundred

    def puzzle_response(self, answer: str) -> str:
        return self.eval_stmt(answer)

    def eval_stmt(self, s) -> str:
        nums = ['trash', 'dogshit', 'garbage']
        lst = []
        rtn =''
        for char in s:
            if char in '0123456789':
                return 'ARITHMATIC ERROR'
        s = self.clean_stmt(s)
        try:
            i  = eval(s)
            if not isinstance(i, int):
                return 'ARITHMATIC ERROR'
            if i == 0:
                return nums[0]
            if i < 0:
                rtn += '-'
                i *= -1
            while i:
                i, r = divmod(i, 3)
                lst.append(nums[r])
            rtn += ''.join(reversed(lst))
            return rtn
        except:
            return 'ARITHMATIC ERROR'

    def clean_stmt(self, s):
        num_lst = []
        tokens = ['trash', 'dogshit', 'garbage', '+', '-', '*', '/']
        rtn = ''
        lst = re.split(r'(trash|dogshit|garbage|\+|-|\*|\/)', s)
        logger.info(lst)
        lst = list(filter(lambda x: x in tokens, lst))
        logger.info(lst)
        for tok in lst:
            if tok == 'trash' or tok == 'dogshit' or  tok == 'garbage':
                num_lst.append(tok)
            else:
                if(num_lst):
                    rtn += str(self.convert_to_num(num_lst))
                rtn += str(tok)
                num_lst = []
        if(num_lst):
            rtn += str(self.convert_to_num(num_lst))
        return rtn

    def convert_to_num(self, lst):
        rtn = 0
        nums = {
                'trash': 0,
                'dogshit' : 1,
                'garbage' : 2
            }
        i = len(lst) - 1
        while(i >= 0):
            rtn += nums[lst[i]] * 3 ** ( len(lst) - 1 - i)
            i -= 1
        return rtn
