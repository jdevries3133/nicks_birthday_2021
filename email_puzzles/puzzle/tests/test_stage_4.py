import ctypes
from time import sleep
import unittest

from ..stage_4_pre import number


class TestStageFour(unittest.TestCase):

    def test_solution(self):
        """
        You can get the true value of the obscured python object with
        ctypes.
        """
        self.assertEqual(
            ctypes.c_short(number).value,
            1325
        )
        sleep(0.2)  # rate limit
