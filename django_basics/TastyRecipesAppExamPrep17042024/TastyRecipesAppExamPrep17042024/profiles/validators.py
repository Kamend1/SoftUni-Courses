from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CustomMinLengthValidator:
    def __init__(self, min_length, message=None):
        self.min_length = min_length
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Nickname must be at least 2 chars long!"
        else:
            self.__message = value

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError(self.message)


@deconstructible
class FirstLetterCapitalValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Name must start with a capital letter!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value[0].isupper():
            raise ValidationError(self.message)
