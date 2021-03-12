import logging

from .emailer import EmailBot

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    format='%(pathname)s:%(lineno)s\n\t%(module)s::%(message)s'
)

EmailBot().listen()
