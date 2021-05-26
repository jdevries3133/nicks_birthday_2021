import time

import requests

# seconds to wait between api calls.
RATE_LIMIT_SLEEP_TIME = 1

class EmkcApiUnavailable(ConnectionError):
    pass


class ArbitraryExecutor:
    def __init__(self):
        self.last_call = time.time() - RATE_LIMIT_SLEEP_TIME
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
                # the rate limit on this api is broken. Even though we are
                # waiting 0.3s between requests, I still get rate limit
                # exceeded responses. It usually works on the second try,
                # though; hence the recursive solution.
                if self._is_rate_limit_exceeded(res):
                    return self.execute(code, lang, args)
                raise EmkcApiUnavailable(
                    f'Bad response code from code execution API: "{res.json()["message"]}"'
                )
        except requests.exceptions.ConnectionError:
            raise EmkcApiUnavailable(
                'Could not connect to code execution API.'
            )
        return res.json()

    def _is_rate_limit_exceeded(self, response) -> bool:
        return 'Requests limited to 5 per second' in response.json()['message']

    def _await_rate_limit(self) -> None:
        """
        Block until rate limit has been satistifed.
        """
        while time.time() - self.last_call < RATE_LIMIT_SLEEP_TIME:
            pass
        self.last_call = time.time()
