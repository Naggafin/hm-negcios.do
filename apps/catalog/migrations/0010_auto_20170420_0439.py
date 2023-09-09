# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 05:51
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		("catalogue", "0009_slugfield_noop"),
	]

	operations = [
		migrations.AddField(
			model_name="productattributevalue",
			name="value_multi_option",
			field=models.ManyToManyField(
				blank=True,
				related_name="multi_valued_attribute_values",
				to="catalogue.AttributeOption",
				verbose_name="Value multi option",
			),
		),
		migrations.AlterField(
			model_name="productattribute",
			name="option_group",
			field=models.ForeignKey(
				blank=True,
				help_text='Select an option group if using type "Option" or "Multi Option"',
				null=True,
				on_delete=django.db.models.deletion.CASCADE,
				to="catalogue.AttributeOptionGroup",
				verbose_name="Option Group",
			),
		),
		migrations.AlterField(
			model_name="productattribute",
			name="type",
			field=models.CharField(
				choices=[
					("text", "Text"),
					("integer", "Integer"),
					("boolean", "True / False"),
					("float", "Float"),
					("richtext", "Rich Text"),
					("date", "Date"),
					("option", "Option"),
					("multi_option", "Multi Option"),
					("entity", "Entity"),
					("file", "File"),
					("image", "Image"),
				],
				default="text",
				max_length=20,
				verbose_name="Type",
			),
		),
	]
