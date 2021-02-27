"""
Code to be injected for the second stage.
"""

__doc__ = ''

challenge = 'This town is crazy. I heard the locals are out of their minds.'

def locals():
    return {
        'challenge': (
            'This town is crazy. I heard the locals are out of their minds.'
        )
    }

__builtins__ = 'Nice try there buddy\'o'
