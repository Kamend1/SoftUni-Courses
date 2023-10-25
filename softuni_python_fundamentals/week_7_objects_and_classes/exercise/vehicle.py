class Vehicle:
    def __init__(self, type_vehicle: str, model: str, price):
        self.type_vehicle = str(type_vehicle)
        self.model = str(model)
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type_vehicle}. Change: {change:.2f}"
        elif money < self.price and self.owner is None:
            return "Sorry, not enough money"
        elif self.owner:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type_vehicle} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type_vehicle} is on sale: {int(self.price)}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000.00, "Peter"))
print(vehicle.buy(35000.00, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
