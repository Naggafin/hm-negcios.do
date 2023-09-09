from modeltranslation.translator import TranslationOptions, translator

from .models import (
	AttributeOption,
	AttributeOptionGroup,
	Category,
	Option,
	Product,
	ProductAttribute,
	ProductClass,
)


class ProductClassTranslationOptions(TranslationOptions):
	fields = ["name"]


class CategoryTranslationOptions(TranslationOptions):
	fields = ["name", "description", "meta_title", "meta_description"]


class ProductTranslationOptions(TranslationOptions):
	fields = ["title", "description", "meta_title", "meta_description"]


class ProductAttributeTranslationOptions(TranslationOptions):
	fields = ["name"]


class AttributeOptionGroupTranslationOptions(TranslationOptions):
	fields = ["name"]


class AttributeOptionTranslationOptions(TranslationOptions):
	fields = ["option"]


class OptionTranslationOptions(TranslationOptions):
	fields = ["name", "help_text"]


translator.register(AttributeOption, AttributeOptionTranslationOptions)
translator.register(AttributeOptionGroup, AttributeOptionGroupTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductAttribute, ProductAttributeTranslationOptions)
translator.register(ProductClass, ProductClassTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Option, OptionTranslationOptions)
