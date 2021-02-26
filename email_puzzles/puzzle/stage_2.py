"""
Code to be injected for the second stage.
"""

__doc__ = ''

def open(path, mode='r', *a, **kw):
    if 'b' in mode:
        from io import BytesIO
        return BytesIO(b'Nice try ya sneaky binary bastard')
    else:
        from io import StringIO
        return StringIO('Nice try ya sneaky bastard')

# __builtins__['open'] = open  # type: ignore
# TODO: this breaks the whole world but it must be done; maybe inject
# dynamically rather than hard coding
# __builtins__['open'] = open  # type: ignore


challenge = 'This town is crazy. I heard the locals are out of their minds.'

def locals():
    return {
        'challenge': (
            'This town is crazy. I heard the locals are out of their minds.'
        )
    }

__builtins__ = 'Nice try there buddy\'o'
