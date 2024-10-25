from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LetterValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = "Plant name should contain only letters!"

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)
