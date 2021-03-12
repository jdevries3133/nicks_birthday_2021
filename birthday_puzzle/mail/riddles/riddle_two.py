from .base import SimpleRiddle


class RiddleTwo(SimpleRiddle):
    """
    (Thing 1)
    I, at the start, am old
    Many centuries I've been told
    Used by the Greeks
    For counting techniques
    After things were bought and sold

    Later is when I became known
    As an infinite figure, when shown
    You've counted my spaces
    Over two billion places
    And still, my amount is unknown

    (Thing 2)
    I, too, am not young
    I'm almost as old as Thing 1
    I'm just a frog
    On the natural log
    But I can make counting fun

    (Thing 1 and Thing 2)
    When you combine us two
    In the order of Thing 1 and Thing 2
    We'll be a baked treat
    That's painful to beat
    Whether cherry, peach, or aloo

    Format your answer as three words each separated by a new line.

    Solution:
    - Pi
    - E
    - Pie
    """

    def __init__(self):
        super().__init__(stage_id=2)

    @ property
    def CORRECT_ANSWERS(self) -> list:
        return ['pi\ne\npie']
