from .Puzzle import Puzzle
from enum import Enum
import re

class BadMath(Puzzle):

    def check_answer(self, s):
        """
        WARNING: this one takes s as an int
        """
        return self.eval_stmt(s) == 29

    def get_response(self, s):
        for char in s:
            if char in '0123456789':
                return 'ERROR:NaN'
        return self.eval_stmt(s)

    def eval_stmt(self, s):
        self.clean_stmt(s)
        try:
            eval(s)
        except NameError:
            return 'ERROR:NaN'

    def clean_stmt(self, s):
        lst = re.split(r'(trash|dogshit|garbage|+|-|*|/)', s)
        lst = filter(None, lst)
        lst = filter(lambda x: x != " ", lst)
        convert_nums(lst)

    def convert_num(self, lst):
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
