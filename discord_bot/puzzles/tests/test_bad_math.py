import unittest
from .. import BadMath

class TestBadMath(unittest.TestCase):

    def setUp(self):
        self.my_math = BadMath("N/A")

    def test_converter(self):
        lst = ["dogshit", "trash", "trash"]
        assert self.my_math.convert_num(lst) == 9
