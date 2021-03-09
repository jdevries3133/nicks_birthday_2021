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

def now_this_is_metaprogramming(func):
    def wrap(*a, **kw):
        for n1, p1 in a[0].people.items():
            for n2, p2 in a[0].people.items():
                try:
                    func(a[0], p1, p2)
                except Exception as e:
                    raise Exception(
                        f'Above occured on {n1} and {n2} instances'
                    ) from e
        return
    return wrap


class TestStageTwo(TestCase):

    def setUp(self):
        """
        This self.people dict can be helpful for making more descriptive
        error messages and debugging.
        """
        self.people = {
            'forrest': forrest,
            'jack': jack,
            'thomas': thomas,
            'carina': carina,
            'kate': kate,
            'nick': nick
        }

    # --- __add__ ---

    @ now_this_is_metaprogramming
    def test__add__works(self, p1, p2):
        self.assertEqual(
            p1 + p2,
            p2 + p1
        )

    @ now_this_is_metaprogramming
    def test__add__returns_string(self, p1, p2):
        """
        Add everyone to everyone else and make sure we always get a string
        back and no an errors/exceptions.
        """
        self.assertIsInstance(p1 + p2, str)
        self.assertIsInstance(p2 + p1, str)


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

