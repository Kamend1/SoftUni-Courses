from django import template
from MyMusicAppExamPrep1.utils import get_object

register = template.Library()


@register.simple_tag
def show_nav_if_profile():
    return get_object()
