import string
from unittest import TestCase
from unittest.mock import patch

from ..australian_mode import AustralianMode, convert


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
    def test_unlock_console(self):
        """
        Test for the wrapper function at the top.
        """
        self.assertTrue(self.aust.console_unlocked)

    @ unlock_console
    def test_run_all_commands(self):
        """
        WARNING: This test is being run against random output with loose
        assertions.

        Simply calls all the commands 10 times makeing sure that the response
        is popped off the possible_responses list after being called.
        """
        for command, cmd_dict in self.aust.commands.items():
            for _ in range(10):
                response = self.aust.puzzle_response(command)
                self.assertNotIn(
                    convert(response).lower(),
                    [
                        i.lower() for i in cmd_dict['possible_responses']
                    ]
                )
        for cmd_dict in self.aust.commands.values():
            self.assertTrue(cmd_dict['was_executed'])

    @ unlock_console
    @ patch('discord_bot.puzzles.australian_mode.random.randint', return_value=0)
    def test_complete_solution(self, mock_randint):
        """
        For the puzzle to be solved, every puzzle must be called, and every
        success response must be returned. Here, success responses are forced
        to be returned always by mocking randint. In that case, issuing each
        command once will solve the puzzle.
        """
        for command in self.aust.commands:
            self.aust.puzzle_response(command)
        # this is condition will cause the controller to advance to the next
        # puzzle.
        self.assertTrue(self.aust.check_answer(''))

    @ unlock_console
    @ patch('discord_bot.puzzles.australian_mode.random.randint', return_value=1)
    def test_brute_force_solve(self, mock_randint):
        """
        In the worst case, failure messages are popped from the list after
        they are returned, so it should be possible to solve the puzzle
        through repitition rather than simply through luck.

        This test patches randint so that the success response will not be
        chosen until all the failure responses have bene popped off the list
        of possible responses.

        This sumulates the lengthiest possible solution.
        """
        for command, cmd_dict in self.aust.commands.items():
            while len(cmd_dict['possible_responses']) >= 2:
                expected_response = cmd_dict['possible_responses'][1].lower()
                actual_response = self.aust.puzzle_response(command)
                self.assertEqual(
                    convert(actual_response).lower(),
                    expected_response.lower(),
                )
                self.assertNotIn(
                    expected_response.lower(),
                    [i.lower() for i in cmd_dict['possible_responses']]
                )

    @ unlock_console
    def test_post_success_response(self):
        """
        After the puzzle is solved, a simple canned response should be
        provided for that puzzle.
        """
        for command, cmd_dict in self.aust.commands.items():
            cmd_dict['was_executed'] = True
            response = self.aust.puzzle_response(command)
            self.assertEqual(
                convert(response).lower(),
                (
                    'Ya already found success here mate. Don\'t want ya gettin '
                    f'yourself in more trouble with that {command}'
                ).lower()
            )


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
