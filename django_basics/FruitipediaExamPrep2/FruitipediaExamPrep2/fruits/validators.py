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
        if value is None:
            self.__message = "Fruit name should contain only letters!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)