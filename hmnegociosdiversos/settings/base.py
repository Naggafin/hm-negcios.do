"""
Django settings for hmnegociosdiversos project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
	"modeltranslation",
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"django.contrib.sites",
	"django.contrib.flatpages",
	# Project
	"apps.checkout.apps.CheckoutConfig",
	"apps.shipping.apps.ShippingConfig",
	"apps.catalog.apps.CatalogConfig",
	"apps.dashboard.apps.DashboardConfig",
	"apps.dashboard.catalog.apps.CatalogDashboardConfig",
	# Paypal
	"paypal.express.dashboard.apps.ExpressDashboardApplication",
	"paypal.express_checkout.dashboard.apps.ExpressCheckoutDashboardApplication",
	"paypal.payflow.dashboard.apps.PayFlowDashboardApplication",
	# Oscar
	"oscar.config.Shop",
	"oscar.apps.analytics.apps.AnalyticsConfig",
	"oscar.apps.address.apps.AddressConfig",
	"oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
	"oscar.apps.communication.apps.CommunicationConfig",
	"oscar.apps.partner.apps.PartnerConfig",
	"oscar.apps.basket.apps.BasketConfig",
	"oscar.apps.payment.apps.PaymentConfig",
	"oscar.apps.offer.apps.OfferConfig",
	"oscar.apps.order.apps.OrderConfig",
	"oscar.apps.customer.apps.CustomerConfig",
	"oscar.apps.search.apps.SearchConfig",
	"oscar.apps.voucher.apps.VoucherConfig",
	"oscar.apps.wishlists.apps.WishlistsConfig",
	"oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
	"oscar.apps.dashboard.users.apps.UsersDashboardConfig",
	"oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
	"oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
	"oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
	"oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
	"oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
	"oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
	"oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
	"oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
	"oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",
	# 3rd-party apps that Oscar depends on
	"paypal",
	"widget_tweaks",
	"haystack",
	"treebeard",
	"sorl.thumbnail",
	"easy_thumbnails",
	"django_tables2",
	# Django apps that the sandbox depends on
	"django.contrib.sitemaps",
	# 3rd-party apps that the sandbox depends on
	"django_extensions",
]

SITE_ID = 1

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
	# Allow languages to be selected
	"django.middleware.locale.LocaleMiddleware",
	"django.middleware.http.ConditionalGetMiddleware",
	"django.middleware.common.CommonMiddleware",
	# Ensure a valid basket is added to the request instance for every request
	"oscar.apps.basket.middleware.BasketMiddleware",
]

ROOT_URLCONF = "hmnegociosdiversos.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [BASE_DIR / "templates"],
		"APP_DIRS": True,
		"OPTIONS": {
			"context_processors": [
				"django.contrib.auth.context_processors.auth",
				"django.template.context_processors.request",
				"django.template.context_processors.debug",
				"django.template.context_processors.i18n",
				"django.template.context_processors.media",
				"django.template.context_processors.static",
				"django.contrib.messages.context_processors.messages",
				# Oscar specific
				"oscar.apps.search.context_processors.search_form",
				"oscar.apps.checkout.context_processors.checkout",
				"oscar.apps.communication.notifications.context_processors.notifications",
				"oscar.core.context_processors.metadata",
			],
		},
	},
]

WSGI_APPLICATION = "hmnegociosdiversos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": BASE_DIR / "db.sqlite3",
		"ATOMIC_REQUESTS": True,
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
	},
]

AUTHENTICATION_BACKENDS = [
	"oscar.apps.customer.auth_backends.EmailBackend",
	"django.contrib.auth.backends.ModelBackend",
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = (
	("en", _("English")),
	("es", _("Spanish")),
)

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_FINDERS = [
	"django.contrib.staticfiles.finders.FileSystemFinder",
	"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
	BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "mediafiles"
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOCALE_PATHS = [BASE_DIR / "locale"]


# ====================
# Messages contrib app
# ====================

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {messages.ERROR: "danger"}


# Haystack settings
HAYSTACK_CONNECTIONS = {
	"default": {
		"ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
		"PATH": BASE_DIR / "whoosh_index",
	},
}


# ==============
# Oscar settings
# ==============

from oscar.defaults import *

# Meta
# ====

OSCAR_SHOP_NAME = "HM.Negocios Diversos, srl"
OSCAR_SHOP_TAGLINE = _(
	"Supliendo PANELES LED de calidad Y todo tipo de letreros por más de 10 años"
)

OSCAR_DEFAULT_CURRENCY = "USD"

OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_ALLOW_ANON_REVIEWS = False

OSCAR_FROM_EMAIL = "noreply@hmnegocios.do"


# Dashboard
# =========

# Add Payflow dashboard stuff to settings
OSCAR_DASHBOARD_NAVIGATION.append(
	{
		"label": _("PayPal"),
		"icon": "icon-globe",
		"children": [
			{
				"label": _("PayFlow transactions"),
				"url_name": "payflow_dashboard:paypal-payflow-list",
			},
			{
				"label": _("Express transactions"),
				"url_name": "express_dashboard:paypal-express-list",
			},
			{
				"label": _("Express Checkout transactions"),
				"url_name": "express_checkout_dashboard:paypal-transaction-list",
			},
		],
	}
)


# Order processing
# ================

# Sample order/line status settings. This is quite simplistic. It's like you'll
# want to override the set_status method on the order object to do more
# sophisticated things.
OSCAR_INITIAL_ORDER_STATUS = "Pending"
OSCAR_INITIAL_LINE_STATUS = "Pending"

# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
	"Pending": (
		"Being processed",
		"Cancelled",
	),
	"Being processed": (
		"Complete",
		"Cancelled",
	),
	"Cancelled": (),
	"Complete": (),
}

# This dict defines the line statuses that will be set when an order's status
# is changed
OSCAR_ORDER_STATUS_CASCADE = {
	"Being processed": "Being processed",
	"Cancelled": "Cancelled",
	"Complete": "Shipped",
}

# Sorl
# ====

THUMBNAIL_KEY_PREFIX = "hmnegocios-diversos"
THUMBNAIL_KVSTORE = "sorl.thumbnail.kvstores.cached_db_kvstore.KVStore"
THUMBNAIL_REDIS_URL = None


# Django 1.6 has switched to JSON serializing for security reasons, but it does not
# serialize Models. We should resolve this by extending the
# django/core/serializers/json.Serializer to have the `dumps` function. Also
# in tests/config.py
SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"


# PayPal

# Taken from PayPal's documentation - these should always work in the sandbox
PAYPAL_API_VERSION = "119"

PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = OSCAR_DEFAULT_CURRENCY
PAYPAL_CUSTOMER_SERVICES_NUMBER = "+1 800-555-5555"
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	"version": 1,
	"disable_existing_loggers": True,
	"formatters": {
		"verbose": {
			"format": "%(levelname)s %(asctime)s %(module)s %(message)s",
		},
		"simple": {"format": "[%(asctime)s] %(message)s"},
	},
	"root": {
		"level": "DEBUG",
		"handlers": ["console"],
	},
	"handlers": {
		"null": {
			"level": "DEBUG",
			"class": "logging.NullHandler",
		},
		"console": {
			"level": "DEBUG",
			"class": "logging.StreamHandler",
			"formatter": "simple",
		},
	},
	"loggers": {
		"oscar": {
			"level": "DEBUG",
			"propagate": True,
		},
		"oscar.catalogue.import": {
			"handlers": ["console"],
			"level": "INFO",
			"propagate": False,
		},
		"oscar.alerts": {
			"handlers": ["null"],
			"level": "INFO",
			"propagate": False,
		},
		# Django loggers
		"django": {
			"handlers": ["null"],
			"propagate": True,
			"level": "INFO",
		},
		"django.request": {
			"handlers": ["console"],
			"level": "ERROR",
			"propagate": True,
		},
		"django.db.backends": {
			"level": "WARNING",
			"propagate": True,
		},
		"django.security.DisallowedHost": {
			"handlers": ["null"],
			"propagate": False,
		},
		# Third party
		"raven": {
			"level": "DEBUG",
			"handlers": ["console"],
			"propagate": False,
		},
		"sorl.thumbnail": {
			"handlers": ["console"],
			"propagate": True,
			"level": "INFO",
		},
	},
}
