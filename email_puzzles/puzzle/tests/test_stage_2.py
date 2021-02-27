from unittest import TestCase

from ..stage_2 import (
    forrest,
    jack,
    thomas,
    kate
)


class TestStageTwo(TestCase):

    # --- forrest (str) ---

    def test_f(self):
        ...

    # --- jack (set) ---

    def test_j(self):
        ...

    # --- thomas (int) ---

    def test_t(self):
        ...

    # --- kate (dict) ---

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
            str(type({'normal': 'dict'}))
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

