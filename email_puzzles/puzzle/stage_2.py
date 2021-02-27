"""
Code to be injected for the second stage.
"""

__doc__ = ''

challenge = 'This town is crazy. I heard the locals are out of their minds.'

class str(str):
    def __module__(self, *a, **kw):
        """
        This causes type() to not return __main__.str
        """
        return None
    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()

    @ property
    def __class__(self):
        return type

    def __dir__(self):
        return super().__dir__()


forrest = str('I am swole.')

del str










































class set(set):
    def __module__(self, *a, **kw):
        """
        This causes type() to not return __main__.str
        """
        return None
jack = set(['this', 'that'])

del set


class int(int):
    def __module__(self, *a, **kw):
        """
        This causes type() to not return __main__.str
        """
        return None
thomas = int(4)

del int

class dict(dict):
    def __module__(self, *a, **kw):
        """
        This causes type() to not return __main__.str
        """
        return None
kate = dict({'this': 'that', 'num': 1})

del dict
