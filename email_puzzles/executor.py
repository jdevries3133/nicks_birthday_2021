import time

import requests

class EmkcApiUnavailable(ConnectionError):
    pass


class ArbitraryExecutor:
    def __init__(self):
        self.last_call = time.time() - 0.2
        self.session = requests.Session()

    def execute(self, code: str, lang: str='python3', args: list=None) -> dict:
        """
        Execute code with the emkc code execution api. Return the query response
        as a python dict.
        """
        try:
            self._await_rate_limit()
            res = self.session.post(
                'https://emkc.org/api/v1/piston/execute/',
                {
                    "language": lang,
                    "source": code,
                    "stdin": "",
                    "args": args if args else []
                }
            )
            if not res.ok:
                raise EmkcApiUnavailable(
                    f'Bad response code from code execution API: "{res.json()["message"]}"'
                )
        except requests.exceptions.ConnectionError:
            raise EmkcApiUnavailable(
                'Could not connect to code execution API.'
            )
        return res.json()

    def _await_rate_limit(self) -> None:
        """
        Block until rate limit has been satistifed.
        """
        while time.time() - self.last_call < 0.5:
            pass
        self.last_call = time.time()
