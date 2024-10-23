from django import template

from TastyRecipesAppExamPrep17042024.utils import get_profile_object

register = template.Library()


@register.simple_tag
def user_profile():
    return get_profile_object()
