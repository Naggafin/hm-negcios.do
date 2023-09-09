# Generated by Django 2.1.5 on 2019-02-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		("catalogue", "0014_auto_20181115_1953"),
	]

	operations = [
		migrations.AddField(
			model_name="product",
			name="is_public",
			field=models.BooleanField(
				default=True,
				help_text="Show this product in search results and catalogue listings.",
				verbose_name="Is public",
			),
		),
	]
