from django import template

register = template.Library()


@register.filter
def video_thumbnail(value):
	# returns YouTube video preview thumbnail
	id = value.split("=")[-1]
	return f"http://i1.ytimg.com/vi/{id}/default.jpg"
