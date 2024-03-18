from abc import ABC, abstractmethod
from typing import List

from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.price_for_reservation: float = 0.00
        self.is_reserved = False
        self.delicacy_orders: List[Gingerbread: Delicacy, Stolen: Delicacy] = []

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    #helper to calculate income from booths

    def calculate_income(self):
        food_bill = sum(delicacy.price for delicacy in self.delicacy_orders)
        income_generated = self.price_for_reservation + food_bill
        return income_generated