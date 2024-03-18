from typing import List
from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.bill = 0.00
        self.shopping_cart: List[Dessert: Meal, MainDish: Meal, Starter: Meal] = []
        self.ordered_food = []

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] == '0' and len(value) == 10 and value.isdigit():
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")

