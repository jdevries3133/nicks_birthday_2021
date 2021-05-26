"""
Minimal wrapper around the cliensend mail API for this project's purposes.
"""

from base64 import b64encode
import logging
import json
from typing import Union

from requests import Session
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)

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

    def __eq__(self, other):
        for attr in [
                'name', 'addr_line_1', 'addr_line_2', 'city',
                'state', 'zip_code', 'country'
        ]:
            if not getattr(self, attr) == getattr(other, attr):
                return False
        return True

    def __repr__(self):
        return self.data()

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
        'return_addr': 'https://rest.clicksend.com/v3/post/return-addresses'
    }

    def __init__(self, username: str, api_key: str, return_addr: Address):
        self.return_addr = return_addr
        self._return_addr_id = None
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
        if not self._get_or_create_return_addr():
            logger.error('Return address creation failed')
            return False
        if not self._upload(document):
            logger.error(f'File upload failed')
            return False
        if not self._send(address):
            logger.error(f'File sending failed')
            return False
        return True

    def _send(self, address: Address) -> bool:
        """
        Tell clicksend to mail previously uploaded file.
        """
        res = self.session.post(
            self.hrefs['send'],
            json={
                'file_url': self.doc_url,
                'recipients': [
                    {
                        **address.data(),
                        'return_address_id': self._return_addr_id,
                    }
                ]
            }
        )
        if res.ok:
            for recipient in res.json()['data']['recipients']:
                if recipient['status'] != 'SUCCESS':
                    logger.error(
                        f'Letter failed to send to {recipient["address_name"]}'
                    )
                    return False
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
            data=payload
        )
        if not res.ok:
            return False
        self.doc_url = res.json()['data']['_url']
        return True

    def _get_or_create_return_addr(self) -> bool:
        if self._return_addr_id:
            return True
        res = self.session.get(self.hrefs['return_addr'])
        for result in res.json()['data']['data']:
            # check that addresses are the same
            if all([
                self.return_addr.data().get(attr) == result.get(attr)
                for attr in [
                    'address_name', 'address_line_1', 'address_line_2',
                    'address_city', 'address_state', 'address_postal_code',
                    'address_country'
                ]
            ]):
                self._return_addr_id = result['return_address_id']
                return True
        return self._create_return_addr()

    def _create_return_addr(self) -> bool:
        res = self.session.post(
            self.hrefs['return_addr'],
            json=self.return_addr.data()
        )
        if res.ok:
            self._return_addr_id = res.json()['data']['return_address_id']
            return True
        return False



if __name__ == '__main__':

    from pathlib import Path
    import json

    with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
        data = json.load(jsonf)

    send_addr = Address(**data['clicksend']['test_address']['send'])
    return_addr = Address(**data['clicksend']['test_address']['return'])

    sender = ClickSend(
        data['clicksend']['username'],
        data['clicksend']['API_KEY'],
        return_addr
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

    sender.send(doc, send_addr)
