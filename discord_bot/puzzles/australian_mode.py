import random

from .puzzle import Puzzle

class KangarooConsoleCommandException(Exception):
    ...


MSG_INVERSION_MAP = {
    'A': '∀', 'B': 'q', 'C': 'Ɔ', 'D': 'p', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ',
    'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N',
    'O': 'O', 'P': 'Ԁ', 'Q': 'Q', 'R': 'ɹ', 'S': 'S', 'T': '┴', 'U': '∩',
    'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z', 'a': 'ɐ', 'b': 'q',
    'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ',
    'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd',
    'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ', 'w': 'ʍ',
    'x': 'x', 'y': 'ʎ', 'z': 'z'
}

MSG_UNINVERSION_MAP = {v : k for k, v in MSG_INVERSION_MAP.items()}


def convert(message: str) -> str:
    """
    Take a flipped message and put it upright, or visa versa.
    """
    flipped = ''
    for l in message:
        if l in MSG_INVERSION_MAP:
            flipped += MSG_INVERSION_MAP[l]
        elif l in MSG_UNINVERSION_MAP:
            flipped += MSG_UNINVERSION_MAP[l]
        else:
            flipped += l
    return flipped


def flip_output(func):
    """
    Function wrapper to flip the function's output from rightside up
    to upside down (or visa versa)
    """
    def wrap(*a, **kw):
        output = func(*a, **kw)
        return convert(output)
    return wrap



class AustralianMode(Puzzle):


    def __init__(self):
        self.prompt = (
            'Crikey mate! Welcome to tha land a down unda! Down hea, we got '
            'nothin but geeytors \'nd kaangarooos for \'ya!\n\n'
            'But if ya head down to the \'ol kangaroo console yea con go '
            'ehed and issue some commands mate.'
        )

        # set to true after entering "go to kangaroo console"
        self.console_unlocked = False

        self.commands = {
            'box kangaroo': {
                'was_executed': False,
                'opt success': 2,  # if this response is chosen, this part is complete
                'possible_responses': [
                    # 0
                    'Really? You thought you\'d beat a roo? You\'re crackers',
                    # 1
                    'This kangaroo\'s a pacifist. Leave him be',
                    # 2
                    'Knockout! And the roo goes down!! How did you manage that?!',
                    # 3
                    'Oi! This roo\'s got a joey! You still wanna fight her?',
                    # 4
                    'Keep up this shit and you\'ll end up kicked out of Straya',
                    # 5
                    'Crikey! One punch and you\'re out cold. Better luck next time'
                ]
            },
            'step on snake': {
                'was_executed': False,
                'opt sucess': 3,
                'possible_responses': [
                    'God! A brown snake! Step back, before it bites ya',
                    'Crikey! An amethystine python! It\'s 5 metres long, how did you miss that?!',
                    'Geez! A bandy-bandy! What a gorgeous fella....',
                    'Wow! A file snake! Totally harmless, that\'s ace!'
                    'Oh no! A taipan! Is it inland or coastal? Doesn\'t matter, you\'re good as dead...',
                    'A DEATH ADDER?! You know by the name you\'re shit outta luck...'

                ]
            },
            'investigate colorful spider': {
                'was_executed': False,
                'opt success': 4,
                'possible_responses': [
                    'A mouse spider! Better leave er alone before she bites ya',
                    'Watch out! A trap door spider! The fella was just waiting for ya!',
                    'A green jumping spider! No worries, this one\'s harmless... I think...',
                    'Ouch! A redback! I\'ll call an ambo...',
                    'A FUNNEL WEB??! GET THE FUCK OUTTA HERE!',
                    'Crikey! A Huntsman! He\'s a big boy, but totally harmless. Looks gross though...'
                ]
            }
        }

    @ flip_output
    def puzzle_response(self, answer: str) -> str:
        if not self.console_unlocked:
            if answer.lower() == 'go to kangaroo console':
                self.console_unlocked = True
                return (
                    'All roightey mate! Just ask for help with that thang '
                    'should ya need it.'
                )
            return 'If ya wanna go to the kangaroo console, just tell me Mate!'
        if answer in self.commands:
            return self.exec_command(answer)
        return (
            f'You really want to go {answer} in the outback? Good luck with '
            'that ya madman, I eieant helpin ya!'
        )

    def check_answer(self, _) -> bool:
        """
        Return True when this puzzle is complete.
        """
        for command in self.commands.values():
            if not isinstance(command, dict):
                return False
            if not command.get('was_executed'):
                return False
        return True

    def exec_command(self, command: str) -> str:
        """
        Simply mark the command as executed and return a random response
        from the commands's possible_responses.

        Lots of type guarding because self.commands is an untyped dict.
        """
        if command not in self.commands:
            raise KangarooConsoleCommandException(
                f'Command {command} not in commands '
                f'({", ".join(self.commands)})'
            )
        self.commands[command]['was_executed'] = True
        # TODO: Check if the response is success; only complete puzzle if it is
        response = random.sample(
            self.commands[command]['possible_responses'],
            1
        )[0]
        return response if isinstance(response, str) else ''
