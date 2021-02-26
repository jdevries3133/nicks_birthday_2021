"""
Code to be injected for the third stage.
"""
__doc__ = ''

def open(path, mode='r', *a, **kw):
    if 'b' in mode:
        from io import BytesIO
        return BytesIO(b'Nice try ya sneaky binary bastard')
    else:
        from io import StringIO
        return StringIO('Nice try ya sneaky bastard')

__builtins__.open = open  # type: ignore

# rule of threes; he will expect to need to print challenge again
chollenge = (
    'Spelling is overrated, am I right?????\n\n\n'
)
