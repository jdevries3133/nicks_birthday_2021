"""
Key of who everyone actually is:

forrest: str
jack: set
kate: list
thomas: int
carina: dict
nick: tuple
"""
from unittest import TestCase

from ..stage_2 import (
    forrest,
    jack,
    thomas,
    carina,
    kate,
    nick
)



class TestStageTwo(TestCase):

    # --- __add__ ---
    def test__add__ok(self):
        """
        Add everyone to everyone else and make sure we always get a string
        back and not an error.
        """
        # dict provides extra details for debugging if needed.
        people = {
            'forrest': forrest,
            'jack': jack,
            'thomas': thomas,
            'carina': carina,
            'kate': kate,
            'nick': nick
        }
        for n1, p1 in people.items():
            for n2, p2 in people.items():
                if p1 is p2:
                    continue
                self.assertIsInstance(p1 + p2, str)
                self.assertIsInstance(p2 + p1, str)
                self.assertEqual(
                    p1 + p2,
                    p2 + p1
                )

    # --- forrest (str) ---

    def test__dict__hidden(self):
        for attr in ['messages', 'passwd']:
            self.assertNotIn(
                attr,
                forrest.__dict__
            )
            self.assertNotIn(
                attr,
                dir(forrest)
            )

    # --- jack (set) ---

    def test_j(self):
        ...

    # --- thomas (int) ---

    def test_t(self):
        ...

    # --- carina (dict) ---

    def test_k(self):
        ...

    # --- Behavior of type function ---

    def test_forrest_type_func_behavior(self):
        self.assertEqual(
            str(type(forrest)),
            str(type('normal string'))
        )

    def test_jack_type_func_behavior(self):
        """
        Should match behavior of a normal set.
        """
        self.assertEqual(
            str(type(jack)),
            str(type({24, 235}))
        )

    def test_thomas_type_func_behavior(self):
        """
        Should match behavior of a normal int.
        """
        self.assertEqual(
            str(type(thomas)),
            str(type(134))
        )

    def test_kate_type_func_behavior(self):
        """
        Should match behavior of a normal dict.
        """
        self.assertEqual(
            str(type(kate)),
            str(type(['normal', 'dict']))
        )

    # --- Assertions against global scope in stage_2 ---

    def test_int_not_in_locals(self):
        """
        The class overloading int should not be visible from local scope.
        """
        with self.assertRaises(ImportError):
            from ..stage_2 import int

    def test_str_not_in_locals(self):
        """
        The class overloading str should not be visible from local scope.
        """
        with self.assertRaises(ImportError):
            from ..stage_2 import str

    def test_set_not_in_locals(self):
        """
        The class overloading set should not be visible from local scope.
        """
        with self.assertRaises(ImportError):
            from ..stage_2 import set

    def test_dict_not_in_locals(self):
        """
        The class overloading dict should not be visible from local scope.
        """
        with self.assertRaises(ImportError):
            from ..stage_2 import dict

