"""
Wrapper class for ClickSend API
"""

import json
from base64 import b64encode
from pathlib import Path

import requests


# TODO: I need to generate a pdf or docx file on the fly to use this API


with open(Path(Path(__file__).parent, 'secrets.json'), 'r') as jsonf:
    KEY = json.load(jsonf)['API_KEY']


def send_letter(message: str) -> bool:
    """
    Return a boolean indicating whether the letter was sent.
    """
    response = requests.post(
        'https://rest.clicksend.com/v3/post/letters/send',
        headers={
            'Authorization': b64encode(
                bytes(f'jdevries3133@gmail.com:{KEY}', 'utf-8')
            )
        },
        data={}
    )
    return 200 <= response.status_code <= 299
