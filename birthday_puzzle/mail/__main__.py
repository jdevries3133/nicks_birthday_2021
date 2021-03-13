import logging
from pathlib import Path

from .mailer import Mailer


logging.basicConfig(
    filename=Path(Path(__file__).parents[2], 'mail_bot.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s => %(message)s',
)



Mailer().listen()
