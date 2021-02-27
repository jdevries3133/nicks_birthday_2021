import unittest
from .. import BadMath

class TestBadMath(unittest.TestCase):

    def setUp(self):
        self.my_math = BadMath("N/A")

    # Test to make sure the coverter is properly converting base 3 numbers
    def test_converter(self):
        lst = ["dogshit", "trash", "trash"]
        assert self.my_math.convert_to_num(lst) == 9

    # Test that the clean_stmt function can run for a properly formed package
    def test_clean_statment(self):
        s = "dogshittrashgarbage + dogshit - garbage * garbage"
        s = self.my_math.clean_stmt(s)
        assert s == '11+1-2*2'

    # Test that clean_function does not crash on a malformed package
    def test_clean_statment_on_bad_string(self):
        s = "dogshittrahgarbage + dogsht - garbage * garbage"
        s = self.my_math.clean_stmt(s)

    # Test that +- works for eval
    def test_eval_plusminus(self):
        s = "dogshittrashgarbage + -dogshit - garbage * garbage"
        i = self.my_math.eval_stmt(s)
        assert i == 'garbagetrash'

    # Test that eval works for negitives
    def test_eval_negitive(self):
        s = "-dogshittrashgarbage + -dogshit - garbage * garbage"
        i = self.my_math.eval_stmt(s)
        assert i == '-dogshitgarbagedogshit'
