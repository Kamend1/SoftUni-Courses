from typing import List

from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child


class Room:
    DEFAULT_APPLIANCE_LIST = []

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.appliances = self.DEFAULT_APPLIANCE_LIST
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for arg in args:
            for el in arg:
                total_cost += el.cost
        return round(total_cost * 30, 1)
