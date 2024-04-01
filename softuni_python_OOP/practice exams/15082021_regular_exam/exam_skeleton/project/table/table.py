from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[Bread: BakedFood, Cake: BakedFood] = []
        self.drink_orders: List[Tea: Drink, Water: Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    @property
    @abstractmethod
    def type(self):
        pass

    def reserve(self, number_of_people: int):
        self.number_of_people += number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        sum_food = sum(food.price for food in self.food_orders)
        sum_drinks = sum(drink.price for drink in self.drink_orders)
        total_sum = sum_food + sum_drinks
        return total_sum

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            result = [f"Table: {self.table_number}", f"Type: {self.type}", f"Capacity: {self.capacity}"]

            return "\n".join(result)
