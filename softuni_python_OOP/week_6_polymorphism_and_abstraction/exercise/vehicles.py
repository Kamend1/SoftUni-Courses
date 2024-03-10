from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITION_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity < (self.fuel_consumption + self. AIR_CONDITION_FUEL_CONSUMPTION) * distance:
            return

        self.fuel_quantity -= (self.fuel_consumption + self. AIR_CONDITION_FUEL_CONSUMPTION) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITION_FUEL_CONSUMPTION = 1.6
    RETAIN_FUEL_FACTOR = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity < (self.fuel_consumption + self.AIR_CONDITION_FUEL_CONSUMPTION) * distance:
            return

        self.fuel_quantity -= (self.fuel_consumption + self.AIR_CONDITION_FUEL_CONSUMPTION) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.RETAIN_FUEL_FACTOR

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
