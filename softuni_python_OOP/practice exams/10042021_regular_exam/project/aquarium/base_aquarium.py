from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    VALID_FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[Ornament: BaseDecoration, Plant: BaseDecoration] = []
        self.fish: List[FreshwaterFish: BaseFish, SaltwaterFish: BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    @property
    @abstractmethod
    def type(self):
        pass

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.type in self.VALID_FISH_TYPES:
            self.fish.append(fish)
            return f"Successfully added {fish.type} to {self.name}."
        else:
            return "Water not suitable."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f"{self.name}:"]

        if len(self.fish) == 0:
            result.append("Fish: none")
        else:
            result.append(f"Fish: {' '.join(fish.name for fish in self.fish)}")

        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return "\n".join(result)
