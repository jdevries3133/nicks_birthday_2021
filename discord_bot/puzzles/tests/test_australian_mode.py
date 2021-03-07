import string
from unittest import TestCase

from ..australian_mode import AustralianMode, MSG_INVERSION_MAP, convert


def unlock_console(func):
    def wrap(*a, **kw):
        a[0].aust.console_unlocked = True
        return func(*a, **kw)
    return wrap

class TestAustrailanMode(TestCase):

    def setUp(self):
        self.aust = AustralianMode()

    def test_default_response(self):
        response = self.aust.puzzle_response('hello')
        self.assertEqual(
            response,
            convert('If ya wanna go to the kangaroo console, just tell me Mate!')
        )

    def test_unlock_kangaroo_console(self):
        self.assertFalse(self.aust.console_unlocked)
        response = self.aust.puzzle_response(
            'go to kangaroo console'
        )
        self.assertTrue(self.aust.console_unlocked)

    def test_must_unlock_console(self):
        """
        It should not be possible to execute commands before the console
        is unlocked.
        """
        response = self.aust.puzzle_response('box kangaroo')
        self.assertEqual(
            response,
            convert(
                'If ya wanna go to the kangaroo console, just tell me Mate!'
            )
        )

    @ unlock_console
    def test_commands(self):
        """
        WARNING: This test is being run against random output with loose
        assertions.
        """
        self.assertTrue(self.aust.console_unlocked)
        for command in self.aust.commands:
            for _ in range(10):
                response = self.aust.puzzle_response(command)
                self.assertIn(
                    convert(response),
                    self.aust.commands[command]['possible_responses']
                )
                self.assertTrue(
                    self.aust.commands['box kangaroo']['was_executed']
                )

    @ unlock_console
    def test_complete_solution(self):
        """
        Executing each command once should cause the puzzle to be solved.
        """
        for command in self.aust.commands:
            self.aust.puzzle_response(command)
        self.assertTrue(self.aust.check_answer(''))


def test_convert():
    """
    Test the function to convert strings from right-side-up to upside
    down.

    IMPORTANT! Note that case sensitivty CANNOT be preserved always.
    """
    normal = string.printable[10:62]
    flip = 'ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z'
    assert flip == convert(normal)
    # Case cannot be preserved always!
    assert normal.lower() == convert(flip).lower()

    normal = 'what is up?'
    flip = 'ʍɥɐʇ ᴉs nd?'
    assert flip == convert(normal)
    assert convert(convert(flip)) == flip

