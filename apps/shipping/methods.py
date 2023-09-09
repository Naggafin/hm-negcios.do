from django.utils.translation import gettext_lazy as _
from moneyed import Money
from oscar.apps.shipping import methods
from oscar.core import prices



class Standard(methods.Base):
	code = "standard"
	name = _("Standard shipping")
	shipping_rate = Money(amount="35", currency="USD")

	def calculate(self, basket):
		# conversion_rate = get_conversion_rate(str(self.shipping_rate.currency), basket.currency)
		amount = self.shipping_rate.amount  # * conversion_rate
		return prices.Price(currency=basket.currency, excl_tax=amount, incl_tax=amount)


class International(methods.Base):
	code = "international"
	name = _("International shipping")
	shipping_rate = Money(amount="75", currency="USD")

	def calculate(self, basket):
		# conversion_rate = get_conversion_rate(str(self.shipping_rate.currency), basket.currency)
		amount = self.shipping_rate.amount  # * conversion_rate
		return prices.Price(currency=basket.currency, excl_tax=amount, incl_tax=amount)
