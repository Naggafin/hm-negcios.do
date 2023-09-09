from oscar.apps.shipping import repository

from . import methods


class Repository(repository.Repository):
	def get_available_shipping_methods(
		self, basket, user=None, shipping_addr=None, request=None, **kwargs
	):
		return (
			(methods.Standard(),)
			if shipping_addr and shipping_addr.country.code == "DO"
			else (methods.International(),)
		)
