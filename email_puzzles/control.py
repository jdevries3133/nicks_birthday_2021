# TODO: ask Thomas about persistent storage.
from pathlib import Path

from .executor import ArbitraryExecutor

class Controller:
    """
    Take a message, prepare the puzzle script, execute the puzzle script
    remotely, and return a response message. Also keep track of which puzzles
    have been solved to know which add-ons to append to the base puzzle.
    """
    def __init__(self):
        self.cur_puzzle = 1
        self.num_puzzles = 4
        self.puzzle_dir = Path(Path(__file__).parent, 'puzzle')
        self.executor = ArbitraryExecutor()

    def __iter__(self):
        return self

    def __next__(self):
        self.cur_puzzle += 1
        return self.cur_puzzle

    def respond_to(self, message: str) -> str:
        response = self.executor.execute(self.make_code(message))
        return self._handle_output(
            response['stdout'],
            response['stderr']
        )

    def make_code(self, message: str) -> str:
        return self._exec_before() + message + self._exec_after()

    @ staticmethod
    def _handle_output(stdout: str, stderr: str, ) -> str:
        """
        Depending on the puzzle, stdout can be cleaned up here before being
        sent back to Nick.
        """
        return stdout if not stderr else '\n'.join((stdout, stderr))

    def _exec_before(self) -> str:
        """
        Create the string of python code that will be executed before
        Nick's code.
        """
        with open(Path(self.puzzle_dir, 'base.py'), 'r') as basef:
            exec_before = basef.read()

        for stage_id in range(self.cur_puzzle):
            if stage_id:
                with open(
                    Path(
                        self.puzzle_dir,
                        f'stage_{stage_id}_pre.py'
                    ), 'r'
                ) as stagef:
                    exec_before += '\n' + stagef.read()
        return exec_before

    def _exec_after(self) -> str:
        """
        Create the string of python code that will be executed after Nick's
        code.
        """
        exec_after = ''
        with open(
            Path(self.puzzle_dir, f'stage_{self.cur_puzzle}_post.py'),
            'r'
        ) as stagef:
            exec_after += '\n' + stagef.read()

        with open(Path(self.puzzle_dir, 'cleanup.py'), 'r') as stagef:
            exec_after += stagef.read()
        return exec_after
