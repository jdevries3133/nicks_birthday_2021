from pathlib import Path

from .executor import ArbitraryExecutor
from .puzzle import break_workarounds

class Controller:
    """
    Take a message, prepare the puzzle script, execute the puzzle script
    remotely, and return a response message. Also keep track of which puzzles
    have been solved to know which add-ons to append to the base puzzle.
    """

    puzzle_solutions = {
        '1': {
            'stdout': 'Hello, world!',
            'stderr': '',
            'success_response': 'Hello to you too! Welcome to stage two :)'
        },
        '2': {
            'stdout': '',
            'stderr': '',
            'success_response': ''
        },
        '3': {
            'stdout': '',
            'stderr': '',
            'success_response': ''
        },
        '4': {
            'stdout': '1325',
            'stderr': '',
            'success_response': 'You done it!'
        },
    }

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
        return self._exec_before() + message

    def _handle_output(self, stdout: str, stderr: str, ) -> str:
        """
        Depending on the puzzle, stdout can be cleaned up here before being
        sent back to Nick.
        """
        if (
            stdout
            == self.puzzle_solutions[str(self.cur_puzzle)]['stdout']
        ) and (
            stderr
            == self.puzzle_solutions[str(self.cur_puzzle)]['stderr']
        ):
            next(self)
            return self.puzzle_solutions[str(self.cur_puzzle - 1)]['success_response']
        return stdout if not stderr else '\n'.join((stdout, stderr))

    def _exec_before(self) -> str:
        """
        Create the string of python code that will be executed before
        Nick's code.
        """
        # code snippet to prevent premature puzzle solving
        exec_before = break_workarounds.restrict_builtins
        for stage_id in range(1, self.cur_puzzle + 1):
            if stage_id:
                with open(
                    Path(
                        self.puzzle_dir,
                        f'stage_{stage_id}.py'
                    ), 'r'
                ) as stagef:
                    exec_before += '\n' + stagef.read()
        return exec_before
