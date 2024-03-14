from abc import ABC, abstractmethod
from typing import List


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self. advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Team name cannot be empty!")
        
        self.__name = value
    
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        string_budget = f"{self.budget:.2f}"
        total_equipment_price = 0
        total_protection = 0

        for equipment in self.equipment:
            total_equipment_price += equipment.price
            total_protection += equipment.protection

        total_equipment_price_str = f"{sum(equipment.price for equipment in self.equipment):.2f}"
        average_protection = 0
        if self.equipment:
            average_protection = str(int(total_protection / len(self.equipment)))

        result = ("Name: " + self.name + "\n" +
                  "Country: " + self.country + "\n" +
                  "Advantage: " + str(self.advantage) + " points\n" +
                  "Budget: " + string_budget + "EUR\n" +
                  "Wins: " + str(self.wins) + "\n" +
                  "Total Equipment Price: " + total_equipment_price_str + "\n" +
                  "Average Protection: " + str(average_protection)
                  )

        return result
