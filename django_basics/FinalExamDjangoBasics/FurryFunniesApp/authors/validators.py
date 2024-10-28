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
            self.__message = "Your name must contain letters only!"

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PassCodeValidator:

    def __init__(self, exact_length, message=None):
        self.message = message
        self.exact_length = exact_length

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = "Your passcode must be exactly 6 digits!"

    def __call__(self, value):
        if not value.isdigit() or len(value) != self.exact_length:
            raise ValidationError(self.message)
