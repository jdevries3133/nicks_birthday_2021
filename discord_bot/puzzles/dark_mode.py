from .puzzle import Puzzle


class DarkMode(Puzzle):
    """
    "Dark Mode"; i.e. we can't see anything and therefore need to use braille.
    The cypher text is actually first encrypted a ROT[n] cyphers then
    translated into braille as to not make things too easy.

    Original Message:

    Ah don't you just wish it could be a short message for once?  If this
    message were not padded out by a bunch of bs, you could probably solve it
    in just a few minutes! But alas, I like to talk. I like to ramble, can you
    blame me? I might be a blind old man but so what. That doesn't mean you ca
    't hear my stories. That doesn't mean I have more to write. Who decided
    that sight must be the gatekeeper to literature all along? What is the
    fairness of requiring sight simply to process information efficiently? The
    world is cruel. CRUEL I TELL YOU!  Anyway, you probably have heard enough
    of my diatribe. The phrase you need to type is tisket a biscuit the baker
    has a dog.Well, I hope you enjoyed this journey. It was quite an adventure
    we had together. So many cypher texts. In the mean time, here is a decoy
    that you might think is what you need to type in, but it is not!

    NEXT LEVEL: "312_NONSENSE_GOTCHA"
    """

    MESSAGE = (
        # give the poor man a little help here
        "This is one rotten message... I hope you enjoy it! "

        # rot13
        "Nu qba'g lbh whfg jvfu vg pbhyq or n fubeg zrffntr sbe bapr?"

        # rot12
        " Ur ftue yqeemsq iqdq zaf bmppqp agf nk m ngzot ar ne, kag oagxp "
        "bdanmnxk eaxhq uf uz vgef m rqi yuzgfqe! "

        # rot11
        "Mfe lwld, T wtvp ez elwv. T wtvp ez clxmwp, nly jzf mwlxp xp? T xtrse "
        "mp l mwtyo zwo xly mfe dz hsle. "

        # rot10
        "Drkd nyocx'd wokx iye mkx'd rokb wi cdybsoc. Drkd nyocx'd wokx S rkfo "
        "wybo dy gbsdo. "

        # rot9
        "Fqx mnlrmnm cqjc brpqc vdbc kn cqn pjcntnnyna cx urcnajcdan juu "
        "juxwp? Fqjc rb cqn ojrawnbb xo anzdrarwp brpqc brvyuh cx yaxlnbb "
        "rwoxavjcrxw noorlrnwcuh? Cqn fxaum rb ladnu. LADNU R CNUU HXD!"

        # rot13
        "Naljnl, lbh cebonoyl unir urneq rabhtu bs zl qvngevor. Gur cuenfr lbh "
        "arrq gb glcr vf, "

        # rot23
        "qfphbq x yfpzrfq qeb yxhbo exp x ald."

        # rot18
        "Owdd, A zghw qgm wfbgqwv lzak bgmjfwq. Al osk imalw sf svnwflmjw ow "
        "zsv lgywlzwj. Kg esfq uqhzwj lwplk. Af lzw ewsf laew, zwjw ak s vwugq "
        "lzsl qgm eayzl lzafc ak ozsl qgm fwwv lg lqhw af, tml al ak fgl!"
        'FWPL DWNWD: "312_FGFKWFKW_YGLUZS"'
    )

    def __init__(self):
        self.prompt = (
            'Ah shit oh fuck we\'re in dark mode now; I can\'t see shit in '
            'here! We\'re gonna need a communication method suitable for '
            'those without sight!'
        )

    def puzzle_response(self, answer: str) -> str:
        ...

    def check_answer(self, answer: str) -> bool:
        ...
