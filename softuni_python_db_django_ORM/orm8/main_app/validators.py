from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    menu_categories = ["Appetizers", "Main Course", "Desserts"]

    for category in menu_categories:
        if category not in value:
            raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
