from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class YearValidator:
    def __init__(self, min_year=1999, max_year=2030, message=None):
        self.min_year = min_year
        self.max_year = max_year
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = f"Year must be between {self.min_year} and {self.max_year}!"

    def __call__(self, value):
        if value < self.min_year or value > self.max_year:
            raise ValidationError(self.message)
