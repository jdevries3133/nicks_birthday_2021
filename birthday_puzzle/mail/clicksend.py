"""
Minimal wrapper around the cliensend mail API for this project's purposes.
"""

from base64 import b64encode
from re import A
from typing import Union

from requests import Session
from requests.auth import HTTPBasicAuth


class Address:
    def __init__(self, *,
        name: str,
        addr_line_1: str,
        addr_line_2: Union[str, None],
        city: str,
        state: str,
        zip_code: int
    ):
        self.name = name
        self.addr_line_1 = addr_line_1
        self.addr_line_2 = addr_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code


class ClickSend:

    hrefs = {
        'upload': 'https://rest.clicksend.com/v3/uploads',
        'send': 'https://res.clicksend.com/v3/post/letters/send',
    }

    def __init__(self, username: str, api_key: str):
        self.session = Session()
        self.session.auth = HTTPBasicAuth(username, api_key)

    def send(self, document: bytes, address: Address) -> bool:
        """
        Send a word of pdf file through the clicksend mail api. This function
        does two things:

        1. Upload the document
        2. Send the mail

        Returns a boolean indicating whether the action was successful.
        """

        # upload to clicksend API
        payload = b'{"content":"' + b64encode(document) + b'"}'
        res = self.session.post(
            self.hrefs['upload'],
            params={'convert': 'post'},
            headers={
                'Content-type': 'application/json'
            },
            data=payload
        )
        breakpoint()
        if not self.is_successful(res):
            return False
        return True

    @ staticmethod
    def is_successful(response):
        return 200 <= response.status_code <= 299

if __name__ == '__main__':

    from pathlib import Path
    import json

    with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
        data = json.load(jsonf)

    addr = Address(
        name=data['clicksend']['name'],
        addr_line_1=data['clicksend']['addr1'],
        addr_line_2=data['clicksend']['addr2'],
        city=data['clicksend']['city'],
        state=data['clicksend']['state'],
        zip_code=data['clicksend']['zip_code']
    )
    
    sender = ClickSend(
        data['clicksend']['username'],
        data['clicksend']['API_KEY']
    )
    with open(
        Path(
            Path(__file__).parent,
            'riddles',
            'static',
            '1',
            '1_initial.docx'
        ),
        'rb'
    ) as docf:
        doc = docf.read()

    sender.send(doc, addr)