import ctypes
from time import sleep
import unittest
from unittest.mock import patch

from ..stage_3 import number


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

    def test_tricky_int_not_in_namespace(self):
        """
        Make the puzzle the tricker by hiding the int implementation.
        """
        with self.assertRaises(ImportError):
            from ..stage_3 import int
