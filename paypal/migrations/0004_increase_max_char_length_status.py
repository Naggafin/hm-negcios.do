# Generated by Django 3.0.12 on 2021-02-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		("paypal", "0003_expresscheckouttransaction"),
	]

	operations = [
		migrations.AlterField(
			model_name="expresscheckouttransaction",
			name="status",
			field=models.CharField(max_length=255),
		),
	]
