from oscar.apps.dashboard.catalogue.forms import ProductForm as OscarProductForm


class ProductForm(OscarProductForm):
	class Meta(OscarProductForm.Meta):
		fields = [
			"title",
			"upc",
			"video_url",
			"description",
			"is_public",
			"is_discountable",
			"structure",
			"slug",
			"meta_title",
			"meta_description",
		]
