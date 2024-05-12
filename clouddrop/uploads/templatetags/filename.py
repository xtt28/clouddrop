import os

from django import template

register = template.Library()


@register.filter
def filename(value):
    return str(os.path.basename(value.data.name)).split(".", 1)[1]
