from salmon import queue
from salmon.routing import Router
from salmon.server import LMTPReceiver, Relay

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from . import settings

# the relay host to actually send the final message to
settings.relay = Relay(host=settings.relay_config['host'],
                       port=settings.relay_config['port'], debug=1)

# where to listen for incoming messages
settings.receiver = LMTPReceiver(settings.receiver_config['host'],
                                 settings.receiver_config['port'])

Router.defaults(**settings.router_defaults)
Router.load(settings.handlers)
Router.RELOAD = True
