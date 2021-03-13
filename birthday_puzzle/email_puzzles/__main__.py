import logging
from pathlib import Path

from .emailer import EmailBot

logging.basicConfig(
    filename=Path(Path(__file__).parents[2], 'email_bot.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(name)s => %(message)s',
)

EmailBot().listen()
