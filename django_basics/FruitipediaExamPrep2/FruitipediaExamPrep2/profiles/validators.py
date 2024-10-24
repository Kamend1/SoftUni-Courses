from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FirstLetterValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must start with a letter!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value[0].isalpha():
            raise ValidationError(self.message)


@deconstructible
class CustomLengthValidator:
    MIN_LENGTH = 8
    MAX_LENGTH = 20

    def __init__(self, message=None, min_length=MIN_LENGTH, max_length=MAX_LENGTH):
        self.message = message
        self.min_length = min_length
        self.max_length = max_length

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "*Password length requirements: 8 to 20 characters"
        else:
            self.__message = value

    def __call__(self, value):
        if not self.min_length <= len(value) <= self.max_length:
            raise ValidationError(self.message)
