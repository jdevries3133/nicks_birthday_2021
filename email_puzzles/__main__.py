import logging

from .emailer import EmailBot

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()]
)

EmailBot().listen()
