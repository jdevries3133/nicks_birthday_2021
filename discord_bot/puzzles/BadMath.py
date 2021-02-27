from .Puzzle import Puzzle
from enum import Enum
import re

class BadMath(Puzzle):

    def check_answer(self, s):
        """
        WARNING: this one takes s as a string
        """
        return self.eval_stmt(s) == 100

    def puzzle_response(self, s):
        return self.eval_stmt(s)

    def eval_stmt(self, s):
        nums = ['trash', 'dogshit', 'garbage']
        lst = []
        rtn =''
        for char in s:
            if char in '0123456789':
                return 'ARITHMATIC ERROR'
        s = self.clean_stmt(s)
        try:
            i  =  eval(s)
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
        except Exception:
            return 'ARITHMATIC ERROR'

    def clean_stmt(self, s):
        num_lst = []
        tokens = ['trash', 'dogshit', 'garbage', '+', '-', '*', '/']
        rtn = ''
        lst = re.split(r'(trash|dogshit|garbage|\+|-|\*|\/)', s)
        print(lst)
        lst = list(filter(lambda x: x in tokens, lst))
        print(lst)
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
