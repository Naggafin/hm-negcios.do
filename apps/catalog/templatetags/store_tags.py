from django.conf import settings
from django.template import Library

register = Library()


@register.simple_tag
def store_tag_line():
	return settings.OSCAR_SHOP_TAGLINE
