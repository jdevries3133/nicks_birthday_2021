"""
Code to be injected for the fourth stage.
"""

__doc__ = ''


class int(int):

    from random import randint

    sassy_responses = [
        'poo poo butthole',
        'bonk! go to operator overlaoding jail!',
        'Don\'t look at me, I\'m shy UwU',
        'who the fuck knows I\'m not paid enough for this shit'
        'va te faire foutre !'
        'you really did that? no fuckin way jose'
        'are you even trying???? cmonnnn'
        'why don\'t you try thinking with your brain instead of your ass'
        'this is why we can\'t have nice things'
        'The number you have reached has been disconnected. Goodbye.'
        'Alexa, play This Is Why We Can\'t Have Nice Things by Taylor Swift.'
        '*Bop It voice* I\'m going to sleep.'
        'I can\'t believe you make more money than me.'
        'okay, try again, for real this time'
    ]

    def sass(self):
        return self.sassy_responses[self.randint(
            0,
            len(self.sassy_responses) - 1  # type: ignore
        )]

    def __getattribute__(self, name, *a, **kw):
        if name in ['sass', 'randint', 'sassy_responses']:
            return super().__getattribute__(name, *a, **kw)
        return self.sass()

    def __abs__(self, *a, **kw):
        return self.sass()

    def __add__(self, *a, **kw):
        return self.sass()

    def __and__(self, *a, **kw):
        return self.sass()

    def __bool__(self, *a, **kw):
        return self.sass()

    def __ceil__(self, *a, **kw):
        return self.sass()

    def __class__(self, *a, **kw):
        return self.sass()

    def __delattr__(self, *a, **kw):
        return self.sass()

    def __dict__(self, *a, **kw):
        return self.sass()

    def __dir__(self, *a, **kw):
        return [self.sass()]

    def __divmod__(self, *a, **kw):
        return self.sass()

    def __doc__(self, *a, **kw):
        return self.sass()

    def __eq__(self, *a, **kw):
        return self.sass()

    def __float__(self, *a, **kw):
        return self.sass()

    def __floor__(self, *a, **kw):
        return self.sass()

    def __floordiv__(self, *a, **kw):
        return self.sass()

    def __format__(self, *a, **kw):
        return self.sass()

    def __ge__(self, *a, **kw):
        return self.sass()

    def __getnewargs__(self, *a, **kw):
        return self.sass()

    def __gt__(self, *a, **kw):
        return self.sass()

    def __hash__(self, *a, **kw):
        return self.sass()

    def __index__(self, *a, **kw):
        return self.sass()

    def __init_subclass__(cls, *a, **kw):
        return cls()

    def __int__(self, *a, **kw):
        return self.sass()

    def __invert__(self, *a, **kw):
        return self.sass()

    def __le__(self, *a, **kw):
        return self.sass()

    def __lshift__(self, *a, **kw):
        return self.sass()

    def __lt__(self, *a, **kw):
        return self.sass()

    def __mod__(self, *a, **kw):
        return self.sass()

    def __module__(self, *a, **kw):
        return self.sass()

    def __mul__ (self, *a, **kw):
        return self.sass()

    def __ne__(self, *a, **kw):
        return self.sass()

    def __neg__(self, *a, **kw):
        return self.sass()

    def __or__(self, *a, **kw):
        return self.sass()

    def __pos__(self, *a, **kw):
        return self.sass()

    def __pow__(self, *a, **kw):
        return self.sass()

    def __radd__(self, *a, **kw):
        return self.sass()

    def __rand__(self, *a, **kw):
        return self.sass()

    def __rdivmod__(self, *a, **kw):
        return self.sass()

    def __reduce__(self, *a, **kw):
        return self.sass()

    def __reduce_ex__(self, *a, **kw):
        return self.sass()

    def __repr__(self, *a, **kw):
        return self.sass()

    def __rfloordiv__(self, *a, **kw):
        return self.sass()

    def __rlshift__(self, *a, **kw):
        return self.sass()

    def __rmod__(self, *a, **kw):
        return self.sass()

    def __rmul__(self, *a, **kw):
        return self.sass()

    def __ror__(self, *a, **kw):
        return self.sass()

    def __round__(self, *a, **kw):
        return self.sass()

    def __rpow__(self, *a, **kw):
        return self.sass()

    def __rrshift__(self, *a, **kw):
        return self.sass()

    def __rshift__(self, *a, **kw):
        return self.sass()

    def __rsub__(self, *a, **kw):
        return self.sass()

    def __rtruediv__(self, *a, **kw):
        return self.sass()

    def __rxor__(self, *a, **kw):
        return self.sass()

    def __setattr__(self, *a, **kw):
        return self.sass()

    def __sizeof__(self, *a, **kw):
        return self.sass()

    def __str__(self, *a, **kw):
        return self.sass()

    def __sub__(self, *a, **kw):
        return self.sass()

    def __subclasshook__(self, *a, **kw):
        return self.sass()

    def __truediv__(self, *a, **kw):
        return self.sass()

    def __trunc__(self, *a, **kw):
        return self.sass()

    def __xor__(self, *a, **kw):
        return self.sass()

    def as_integer_ratio(self, *a, **kw):
        return self.sass()

    def bit_length(self, *a, **kw):
        return self.sass()

    def conjugate(self, *a, **kw):
        return self.sass()

    def denominator(self, *a, **kw):
        return self.sass()

    def from_bytes(self, *a, **kw):
        return self.sass()

    def imag(self, *a, **kw):
        return self.sass()

    def numerator(self, *a, **kw):
        return self.sass()

    def real(self, *a, **kw):
        return self.sass()

    def to_bytes(self, *a, **kw):
        return self.sass()

number = int(1325)
del int

# spelling intentional... rule of threes.
chollenge = 'What is the value of the number?'
