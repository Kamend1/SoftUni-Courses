from project.driver import Driver
from typing import List


class Race:

    def __init__(self, name):
        self.name = name
        self.drivers: List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string!")

        self.__name = value
