from django import template
from WorldOfSpeedAppExamPrep24022024.utils import get_profile_object

register = template.Library()


@register.simple_tag
def get_profile():
    return get_profile_object()
