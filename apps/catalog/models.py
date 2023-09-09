from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
	video_url = models.URLField(
		_("Video URL"),
		help_text=_("YouTube product video link."),
		blank=True,
		null=True,
	)


from oscar.apps.catalogue.models import *  # NOQA isort:skip
