from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


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
        if value is not None:
            self.__message = value
        else:
            self.__message = f"Username must be at least {self.min_length} chars long!"

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError(self.message)


@deconstructible
class CustomRegexValidator:
    REGEX = r'^[a-zA-Z0-9_]+$'
    MESSAGE = "Username must contain only letters, digits, and underscores!"

    def __init__(self, regex=None, message=None):
        self.message = message
        self.regex = regex

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = self.MESSAGE
    
    @property
    def regex(self):
        return self.__regex
    
    @regex.setter
    def regex(self, value):
        if value is not None:
            self.__regex = value
        else:
            self.__regex = self.REGEX

    def __call__(self, value):
        if not re.match(self.regex, value):
            raise ValidationError(self.message)
