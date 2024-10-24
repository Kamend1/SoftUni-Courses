from django import template

from FruitipediaExamPrep2.utils import get_profile_object

register = template.Library()


@register.simple_tag
def profile_object_tag():
    return get_profile_object()
