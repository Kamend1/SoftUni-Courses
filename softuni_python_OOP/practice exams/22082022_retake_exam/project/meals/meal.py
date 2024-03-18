from abc import ABC, abstractmethod


class Meal(ABC):
    TYPE_ = 'Meal'

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string!")
        
        self.__name = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value <= 0.00:
            raise ValueError("Invalid price!")

        self.__price = value

    @abstractmethod
    def details(self):
        pass