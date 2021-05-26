from unittest import TestCase
from unittest.mock import patch

from requests import Session

from ..clicksend import Address, ClickSend


class MockAddress(Address):
    def __init__(self):
        self.name = ''
        self.addr_line_1 = ''
        self.addr_line_2 = ''
        self.city = ''
        self.state = ''
        self.zip_code = ''
        self.country = ''

class MockResponse:

    def __init__(self, status_code: int=200, content: str='mock content'):
        self.status_code = status_code
        self.content = content

    def json(self):
        return {'data': {'_url': self.content}}

    def __getitem__(self, item):
        return self.content

    @ property
    def ok(self):
        return 200 <= self.status_code < 300


@ patch.object(Session, 'get')
class TestClickSend(TestCase):

    def setUp(self):
        self.cs = ClickSend(
            username='',
            api_key='',
            return_addr=MockAddress()
        )

    @ patch.object(Session, 'post', return_value=MockResponse(200))
    def test_upload_file(self, *mocks):
        is_success = self.cs._upload(b'document')
        self.assertTrue(is_success)

    @ patch.object(Session, 'post', return_value=MockResponse(400))
    def test_upload_file_fails(self, *mocks):
        is_success = self.cs._upload(b'document')
        self.assertFalse(is_success)

    @ patch.object(Session, 'post')
    def test_send_fail_conditions(self, mock_session, *mocks):

        # will fail if file upload fails
        mock_session.return_value = MockResponse(400)
        is_success = self.cs.send(b'document', MockAddress())
        self.assertFalse(is_success)

        # will fail if file sending fails after uploading succeeds
        with patch('birthday_puzzle.mail.clicksend.ClickSend._upload', return_value=True):
            is_success = self.cs.send(b'document', MockAddress())
            self.assertFalse(is_success)
