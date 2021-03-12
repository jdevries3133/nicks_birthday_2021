import logging
from .mailer import Mailer

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    format='%(pathname)s:%(lineno)s\n\t%(module)s::%(message)s'
)


Mailer().listen()
