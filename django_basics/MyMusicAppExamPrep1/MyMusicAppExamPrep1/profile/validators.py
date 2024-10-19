from django.core.exceptions import ValidationError
import re

from django.utils.deconstruct import deconstructible


@deconstructible
class UserNameValidator:
    def __init__(self, message=None):
        if message is None:
            self.message = "Ensure this value contains only letters, numbers, and underscore."
        else:
            self.message = message

    def __call__(self, value):
        match_string = r'^\w+$'
        if not re.match(match_string, value):
            raise ValidationError(
                self.message,
                # {'params': value}
            )
