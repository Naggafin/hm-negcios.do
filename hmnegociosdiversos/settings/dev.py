import os

from .base import *

from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DEBUG_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Debug toolbar settings
INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = ["*"]

# Django-oscar

OSCAR_URL_SCHEMA = "http"

# sorl

THUMBNAIL_DEBUG = True

# paypal

PAYPAL_SANDBOX_MODE = True
PAYPAL_CALLBACK_HTTPS = False

PAYPAL_API_USERNAME = os.environ.get("DEBUG_PAYPAL_API_USERNAME")
PAYPAL_API_PASSWORD = os.environ.get("DEBUG_PAYPAL_API_PASSWORD")
PAYPAL_API_SIGNATURE = os.environ.get("DEBUG_PAYPAL_API_SIGNATURE")

PAYPAL_CLIENT_ID = os.environ.get("DEBUG_PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.environ.get("DEBUG_PAYPAL_CLIENT_SECRET")

PAYPAL_PAYFLOW_VENDOR_ID = os.environ.get("DEBUG_PAYPAL_PAYFLOW_VENDOR_ID")
PAYPAL_PAYFLOW_PASSWORD = os.environ.get("DEBUG_PAYPAL_PAYFLOW_PASSWORD")

try:
	from .local import *
except ImportError:
	pass
