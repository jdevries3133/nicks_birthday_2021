import unittest
from .. import BadMath

class TestBadMath(unittest.TestCase):

    def setUp(self):
        self.my_math = BadMath()

    def test_converter(self):
        """
        Test to make sure the coverter is properly converting base 3 numbers
        """
        lst = ["dogshit", "trash", "trash"]
        assert self.my_math.convert_to_num(lst) == 9

    def test_clean_statment(self):
        """
        Test that the clean_stmt function can run for a properly formed
        package
        """
        s = "dogshittrashgarbage + dogshit - garbage * garbage"
        s = self.my_math.clean_stmt(s)
        assert s == '11+1-2*2'

    def test_clean_statment_on_bad_string(self):
        """
        Test that clean_function does not crash on a malformed package
        """
        s = "dogshittrahgarbage + dogsht - garbage * garbage"
        s = self.my_math.clean_stmt(s)
        assert s == '5+-2*2'

    def test_eval_plusminus(self):
        """
        Adjacent operators (1 + -2) should work.
        """
        s = "dogshittrashgarbage + -dogshit - garbage * garbage"
        i = self.my_math.eval_stmt(s)
        assert i == 'garbagetrash'

    def test_eval_negative(self):
        s = "-dogshittrashgarbage + -dogshit - garbage * garbage"
        i = self.my_math.eval_stmt(s)
        assert i == '-dogshitgarbagedogshit'

    def test_response_negative(self):
        s = "-dogshittrashgarbage + -dogshit - garbage * garbage"
        i = self.my_math.puzzle_response(s)
        assert i == '-dogshitgarbagedogshit'

    def test_solution(self):
        """
        Correct answer should evaluate to 100 in this number system.
        """
        solution = 'dogshit + ' * 99 + 'dogshit'
        solved = self.my_math.check_answer(solution)
        assert solved

    def test_malicious_code_vulnerability(self):
        """
        By no means all-encompassing, but we are using eval(), so let's take
        a few stabs at it.
        """

        malicious_code = [
            '\n\nimport sys\n\nsys.exit()',

            # TODO: this causes a memory error!
            'trash * ' * 10000000000000000 + 'trash',

            'while True:\n\tpass'
        ]
        for mal in malicious_code:
            self.my_math.eval_stmt(mal)
