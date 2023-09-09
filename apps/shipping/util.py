from decimal import Decimal

from forex_python.converter import CurrencyRates

c = CurrencyRates()


def get_conversion_rate(base: str, quote: str) -> Decimal:
	if base == quote:
		return Decimal(1)
	return c.get_rate(base, quote)
