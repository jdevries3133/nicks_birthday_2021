"""
Code to be injected for the second stage.

WARNING: this code is almost incomprehensible on it's own, but here is how
you can make sense of it:

- Each "person" is a type. So __add__ and similar methods are checking
  types in order to know how to respond.
- In the corresponding test file (./tests/test_stage_2.py), the docstring
  at the top maps names to types.
- So, as you are reading the code, have that key on a split screen and refer
  to it as you look through...

thomas: int
carina: dict

class int(int):  # this becomes thomas...
    def __add__(self, other):
        if isinstance(other, dict):  # thomas + carina
            return 'Thomas and Carina having a jolly old time'
        ...

Of course this means that in Carina's class you'd see:

class dict(dict):
    def __add__(self, other):
        if isinstance(other, int):
            return other + self

Obviously, messing with these classes can cause infinite recursion errors
or cause (a + b) != (b + a), but there is a test that checks for that, so
just run the test suite after any changes.
"""

__doc__ = ''  # do not make the above visible in local scope

challenge = 'This town is crazy. I heard the locals are out of their minds.'


class str(str):

    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.secret_password = '200 grams of protien a day keeps the skinny thinny away'
        self._jdkaaaaasdff_drinks = 0  # security by obsurity

    def __getattribute__(self, name):
        if name == '__dict__' and self._jdkaaaaasdff_drinks < 9:
            return {'hey': 'grease me up a bit if you want my deets'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __dir__(self):
        """
        Hide the class's objects and methods.
        """
        return super().__dir__()

    def __add__(self, other):
        if isinstance(other, set):
            return other + self
        if isinstance(other, int):
            return other + self
        if isinstance(other, dict):
            return 'SCIENCE'
        if isinstance(other, tuple):
            return 'alcoholic chaos'
        if isinstance(other, list):
            return '#virgoseason'
        if other is self:
            return 'ffoorreesstt'
        return other + self

forrest = str('I am swole.')
del str

def drink_together(*people):
    for person in people:
        if person is forrest:
            forrest._jdkaaaaasdff_drinks += 1
            return forrest, 'yum'


class set(set):
    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.passwd = '200 grams of protien a day keeps the skinny away'

    def __getattribute__(self, name):
        if name == '__dict__':
            return {'no': 'cheating'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __dir__(self):
        """
        Hide the class's objects and methods.
        """
        return super().__dir__()

    def __add__(self, other):
        if isinstance(other, str):
            return 'alcoholic chaos 2: electric bogaloo'
        if isinstance(other, int):
            return '#bros'
        if isinstance(other, dict):
            return 'golden retriever energy'
        if isinstance(other, tuple):
            return 'alcoholic chaos 3: this time, it\'s personal'
        if isinstance(other, list):
            return  """┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈
                        ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
                        ▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈
                        ▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏
                        ▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲
                        ▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕
                        ▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
                        ┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈"""
        if other is self:
            return 'jackjack'


jack = set(['this', 'that'])
del set


class int(int):
    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.passwd = '200 grams of protien a day keeps the skinny away'

    def __getattribute__(self, name):
        if name == '__dict__':
            return {'no': 'cheating'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __dir__(self):
        """
        Hide the class's objects and methods.
        """
        return super().__dir__()

    def __add__(self, other):
        if other is self:
            return 'BIG THOMAS ENERGY'
        if isinstance(other, str):
            return 'Jack #1 fan club'
        if isinstance(other, set):
            return '#bros'
        if isinstance(other, dict):
            return (
                'Kate says: "I am not sure! I feel like that\'s the hardest '
                'one because they\'ve interacted with each other the least..."'
            )
        if isinstance(other, tuple):
            return 'Bezos bitches'
        if isinstance(other, list):
            return """Seid ihr das Essen? Nein, wir sind der Jäger!
            Feuerroter pfeil und bogen...
            踏まれた花の 名前も知らずに
            地に墜ちた落ちた鳥は 風を待ちわびる
            祈ったところで 何も変わらない
            《不本意な現状》を変えるのは 戦う覚悟だ...
            屍踏み越えて
            進む意思を 嗤う豚よ
            家畜の安寧...
            虚偽の繁栄...
            死せる餓狼の「自由」を！
            囚われた屈辱は 反撃の嚆だ
            城壁の其の彼方 獲物を屠る《狩人》
            迸る《殺意》に 其の身を灼きながら
            黄昏に緋を穿つ
            紅蓮の弓矢
            矢を番え追い駈ける 標的は逃がさない
            矢を放ち追い詰める 決して逃がさない
            限界まで引き絞る はち切れそうな弦
            「標的」が息絶えるまで 何度でも放つ
            獲物を殺すのは
            「凶器」でも 技術でもない
            研ぎ澄まされた お前自身の殺意だ
            Wir sind die Jäger 焔のように熱く!
            Wir sind die Jäger 氷のように冷ややかに!
            Wir sind die Jäger 己を矢に込めて!
            Wir sind die Jäger 全てを貫いて征け!
            Angriff auf die Titanen
            Der Junge von einst wird bald zum Schwert greifen
            Wer nur seine Machtlosigkeit beklagt. Kann nichts verändern
            Der Junge von einst wird bald das schwarze Schwert ergreifen
            Hass und Zorn sind eine zweischneidige Klinge
            Bald, eines Tages, wird er dem Schicksal die Zähne zeigen
            何かを変える事が出来るのは
            何かを捨てる事が出来るもの
            何ひとつ「危険性」等 背負わないままで 何かが叶う等...
            暗愚の想定 唯の幻影 今は無謀な勇気も
            「自由」の尖兵 賭けの攻勢
            奔る奴隷に勝利を!
            架せられた不条理は 進撃の嚆だ
            奪われた其の地平「自由」を望むあの日の《少年》
            止めどなき《殺意》に 其の身を侵されながら 宵闇に紫を運ぶ
            冥府の弓矢"""

thomas = int(4)
del int

class dict(dict):
    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.passwd = '200 grams of protien a day keeps the skinny away'

    def __getattribute__(self, name):
        if name == '__dict__':
            return {'no': 'cheating'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __dir__(self):
        """
        Hide the class's objects and methods.
        """
        return super().__dir__()

    def __add__(self, other):
        if other is self:
            return 'Careening'
        return other + self

carina = dict({'this': 'that', 'num': 1})
del dict


class list(list):

    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.passwd = '200 grams of protien a day keeps the skinny away'

    def __getattribute__(self, name):
        if name == '__dict__':
            return {'no': 'cheating'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __dir__(self):
        """
        Hide the class's objects and methods.
        """
        return super().__dir__()

    def __add__(self, other):
        if isinstance(other, dict):
            return 'Gal pals'
        if isinstance(other, tuple):
            return 'Also gal pals'
        if other is self:
            return 'I\'ve been writing on the railroad all the doo dah day'
        return other + self

kate = list('this', 'that')
del list


class tuple(tuple):

    def __init__(self, *a, **kw):
        super().__init__()
        self.passwd_entered = False
        self.messages = ['swole']
        self.passwd = '200 grams of protien a day keeps the skinny away'

    def __getattribute__(self, name):
        if name == '__dict__':
            return {'no': 'cheating'}
        return super().__getattribute__(name)

    def __module__(self, *a, **kw):
        """
        This causes type() to return str instead of __main__.str
        """
        return None

    def __dir__(self):
        """
        Hide the class's objects and methods.
        """
        return super().__dir__()

    def __add__(self, other):
        if isinstance(other, dict):
            return r"""|\_____/|     ////\
                |/// \\\|    /// \\\
                 |/O O\|     |/o o\|
                 d  ^ .b     C  )  D    "A Night Out On The Town"
                  \\m//      | \_/ |
                   \_/        \___/
                 __ooo__    _/<|_|>\_
                /_     _\  / |/\_/\| \
                | \_v_/ | |    |\|    |
                || _/ _/\\| |  |\|  | |
                ||)    ( \| |  |\|  | |
                ||      \ | \\ |\|  | |
                ||  --  |  (())\_/  | |
                ((      |   |___|___|_|
                 |______|   |   Y   |))
                  |-||-|    |   |   |
                  | || |    |   |   |
                  | || |    |   |   |
                  | || |    |___|___|prs
                 /u\||/u\   /qp| |qp\
                (_/\||/\_) (___/ \___)"""
        if other is self:
            return 'Enormous Dickens Richard'
        return other + self


nick = tuple(['this', 'that', 'the other'])
del tuple
