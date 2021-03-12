"""
Using the open function to read the puzzle itself, or using subprocess
to call "cat" will spoil the puzzle. These workarounds must be broken or
otherwise prevented by injecting this code at the start of every script.

To my understanding, most of these problems are solved by restricting available
__builtins__. That will even remove the __import__ function, which means
that nothing can be imported.
"""

restrict_builtins = """
__builtins__ = {
    'print': print,
    'dir': dir,
    'help': help,
    'locals': locals,
    'globals': globals,
    'type': type,
}
"""


if __name__ == '__main__':
    exec(restrict_builtins)
