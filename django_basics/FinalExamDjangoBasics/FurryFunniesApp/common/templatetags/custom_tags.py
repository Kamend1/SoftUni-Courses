from django import template

from FurryFunniesApp.utils import get_author_object

register = template.Library()


@register.simple_tag
def author_object_tag():
    return get_author_object()