from django.core.exceptions import ValidationError

def validate_field_only_names_and_spaces(value):

    for char in value:
        if not (char.isalpha() or char.isspace()):
            raise ValidationError('Name can only contain letters and spaces')

