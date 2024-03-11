from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET = 1000000
    SPONSORS = {}
    RACE_EXPENSE = 0


    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        race_income = 0
        for sponsor in self.SPONSORS.keys():
            for k, v in self.SPONSORS[sponsor].items():
                if race_pos <= k:
                    race_income += v
                    break

        race_revenue = race_income - self.RACE_EXPENSE
        self.budget += race_revenue

        return f"The revenue after the race is {race_revenue}$. Current budget {self.budget}$"
