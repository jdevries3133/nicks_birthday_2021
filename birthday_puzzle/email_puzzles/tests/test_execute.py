import time
import unittest

import pytest

from ..executor import ArbitraryExecutor

@ pytest.mark.slow
class TestArbitraryExecutor(unittest.TestCase):
    """
    Integration test that actually reaches out to the API and ensures code
    is executed.
    """

    @ classmethod
    def setUpClass(cls):
        cls.executor = ArbitraryExecutor()
        return cls

    def test_code_execution(self):
        res = self.executor.execute("print('hi')")
        assert res['ran']
        assert res['output'].strip() == 'hi'
        assert res['stdout'].strip() == 'hi'

    def test_other_lang(self):
        res = self.executor.execute('console.log("hello, there")', lang='javascript')
        assert res['ran']
        assert res['output'].strip() == 'hello, there'
        assert res['stdout'].strip() == 'hello, there'

    def test_multiline_code_with_args(self):
        res = self.executor.execute(
            'import sys\nprint(sys.argv)',
            args=['hello', 'world!']
        )
        assert res['ran']
        assert res['stdout'].endswith("'hello', 'world!']\n")

    def test_rate_limit_followed(self):
        """
        Trying to execute through the same class instance quickly will block
        in order to adhere to the rate limit.
        """
        start = time.time()
        for _ in range(2):
            self.executor._await_rate_limit()
        runtime = time.time() - start
        self.assertGreater(runtime, 0.2)
