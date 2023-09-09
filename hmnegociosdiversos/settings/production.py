import os

from .base import *

from dotenv import load_dotenv

load_dotenv()

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = [
	"www.hm-negocios.do",
	"hm-negocios.do",
]

SESSION_SECURE_COOKIE = True
CSRF_SECURE_COOKIE = True

# Django-oscar

OSCAR_URL_SCHEMA = "https"

# sorl

THUMBNAIL_DEBUG = False

# paypal

PAYPAL_SANDBOX_MODE = False
PAYPAL_CALLBACK_HTTPS = True

PAYPAL_API_USERNAME = os.environ.get("PAYPAL_API_USERNAME")
PAYPAL_API_PASSWORD = os.environ.get("PAYPAL_API_PASSWORD")
PAYPAL_API_SIGNATURE = os.environ.get("PAYPAL_API_SIGNATURE")

PAYPAL_CLIENT_ID = os.environ.get("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.environ.get("PAYPAL_CLIENT_SECRET")

PAYPAL_PAYFLOW_VENDOR_ID = os.environ.get("PAYPAL_PAYFLOW_VENDOR_ID")
PAYPAL_PAYFLOW_PASSWORD = os.environ.get("PAYPAL_PAYFLOW_PASSWORD")

try:
	from .local import *
except ImportError:
	pass
