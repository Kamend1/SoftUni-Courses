from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    MISS_OXYGEN_PERCENT = 0
    DEFAULT_OXYGEN_LEVEL = 0

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Diver name cannot be null or empty!")

        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")

        self.__oxygen_level = value

    def miss(self, time_to_catch: int):
        if self.oxygen_level - round(time_to_catch * self.MISS_OXYGEN_PERCENT, 0) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= round(time_to_catch * self.MISS_OXYGEN_PERCENT, 0)

    def renew_oxy(self):
        self.oxygen_level = self.DEFAULT_OXYGEN_LEVEL

    def hit(self, fish: BaseFish):
        if self.validate_if_enough_oxygen(fish):
            self.catch.append(fish)
            self.competition_points += fish.points

    def validate_if_enough_oxygen(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
            return False

        self.oxygen_level -= fish.time_to_catch
        return True

    def update_health_status(self):
        if self.has_health_issue:
            self.has_health_issue = False
        else:
            self.has_health_issue = True

    def __str__(self):
        return (f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, "
                f"Points earned: {self.competition_points:.1f}]")
