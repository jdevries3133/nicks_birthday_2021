"""
Minimal wrapper around the cliensend mail API for this project's purposes.
"""

from base64 import b64encode
import json
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
        zip_code: int,
        country: str='USA'
    ):
        self.name = name
        self.addr_line_1 = addr_line_1
        self.addr_line_2 = addr_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def data(self) -> dict:
        return {
            'address_name': self.name,
            'address_line_1': self.addr_line_1,
            'address_line_2': self.addr_line_2,
            'address_city': self.city,
            'address_state': self.state,
            'address_postal_code': self.zip_code,
            'address_country': self.country
        }


class ClickSend:

    hrefs = {
        'upload': 'https://rest.clicksend.com/v3/uploads',
        'send': 'https://rest.clicksend.com/v3/post/letters/send',
    }

    def __init__(self, username: str, api_key: str):
        self.session = Session()
        self.session.auth = HTTPBasicAuth(username, api_key)
        self.session.headers['Content-Type'] = 'application/json'
        self.doc_url = ''

    def send(self, document: bytes, address: Address) -> bool:
        """
        Send a word of pdf file through the clicksend mail api. This function
        does two things:

        1. Upload the document
        2. Send the mail

        Returns a boolean indicating whether the action was successful.
        """
        if not self._upload(document):
            return False
        if not self._send(address):
            return False
        return True

    def _send(self, address: Address) -> bool:
        """
        Tell clicksend to mail previously uploaded file.
        """
        res = self.session.post(
            self.hrefs['send'],
            data=json.dumps({
                'file_url': self.doc_url,
                'recipients': [
                    address.data(),
                ]
            })
        )
        if self.is_successful(res):
            return True
        return False

    def _upload(self, doc: bytes) -> bool:
        """
        Upload to clicksend API
        """
        payload = b'{"content":"' + b64encode(doc) + b'"}'
        res = self.session.post(
            self.hrefs['upload'],
            params={'convert': 'post'},
            headers={
                'Content-type': 'application/json'
            },
            data=payload
        )
        if not self.is_successful(res):
            return False
        self.doc_url = res.json()['data']['_url']
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
