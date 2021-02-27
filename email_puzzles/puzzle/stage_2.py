"""
Code to be injected for the second stage.

Design Ideas:

Each person has a set of messages that are returned by __repr__ in a cycle;
iterating to the next after each call.

Some methods may be exposed as an interface for two people to interact
or change each others' states.

There can be utility functions sitting in local scope that allow you to
put two people into a situation and see what will happen.

ASCII drawings???

Ultimately, there will be a loosely directed flow of interactions that
must happen in order to reach the end of the puzzle.
"""

__doc__ = ''

challenge = 'This town is crazy. I heard the locals are out of their minds.'


# TODO: there should directions or something. I am restricting access in
# certain ways, but requiring introspection and investigation in others.
# I should clarify which methods or functions are part of the puzzle,
# and which are part of the "walled garden," and won't work / have been
# disabled.

class str(str):

    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.passwd = '200 grams of protien a day keeps the skinny away'

    def __getattribute__(self, name):
        if name == '__dict__':
            return {'hey': 'you are not privy to that information my guy'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()

    def __dir__(self):
        """
        Slightly hide the class's objects and methods.
        """
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


