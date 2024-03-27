from abc import ABC, abstractmethod
from typing import List


class Astronaut(ABC):
    OXYGEN_PER_BREATH = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @property
    @abstractmethod
    def type(self):
        pass

    def breathe(self):
        self.oxygen -= self.OXYGEN_PER_BREATH

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __str__(self):
        if len(self.backpack) > 0:
            backpack_item = ', '.join(self.backpack)
        else:
            backpack_item = 'none'

        result = (f"Name: {self.name}\n"
                  f"Oxygen: {self.oxygen}\n"
                  f"Backpack items: {backpack_item}")

        return result
