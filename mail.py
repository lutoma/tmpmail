from salmon.routing import stateless, route
from models import Email
import platform


@route("(address)@(host)", address=".+")
@stateless
def STORE_MAIL(message, address=None, host=None):
	Email.create(
		node=platform.node(),
		raw=str(message),
		header_src=message['From'],
		envelope_src=message.From,
		dst=message.To,
		subject=message['Subject'],
		headers=dict(message),
		text=message.body())

	return STORE_MAIL
