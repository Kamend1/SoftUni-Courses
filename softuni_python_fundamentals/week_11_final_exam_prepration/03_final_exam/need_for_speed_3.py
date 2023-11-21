class Car:
    def __init__(self, model: str, mileage: int, fuel: int, sold=False):
        self.model = model
        self.mileage = mileage
        self.fuel = fuel
        self.sold = sold

    def drive(self, miles: int, fuel_spent: int):
        result = ""
        if fuel_spent > self.fuel:
            result = "Not enough fuel to make that ride"
        else:
            result =  f"{self.model} driven for {miles} kilometers. {fuel_spent} liters of fuel consumed."
            self.mileage += miles
            self.fuel -= fuel_spent
            if self.mileage > 100000:
                self.sold = True
                result += f"\nTime to sell the {self.model}!"
        return result
    def refuel(self, fuel_added: int):
        if self.fuel + fuel_added > 75:
            fuel_added = 75 - self.fuel
            self.fuel = 75
        else:
            self.fuel += fuel_added
        return f"{self.model} refueled with {fuel_added} liters"

    def revert(self, miles_reverted):
        if self.mileage - miles_reverted < 10000:
            self.mileage = 10000
        else:
            self.mileage -= miles_reverted
            return f"{self.model} mileage decreased by {miles_reverted} kilometers"

    def __repr__(self):
        if self.sold == False:
            return f"{self.model} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."

number_of_cars = int(input())
available_cars = {}

for _ in range(number_of_cars):
    model, mileage, fuel = input().split('|')
    current_car = Car(model, int(mileage), int(fuel))
    available_cars[model] = current_car

while True:
    user_command = input().split(" : ")
    if user_command[0] == "Stop":
        break
    elif user_command[0] == "Drive":

        treated_car = available_cars[user_command[1]]
        result = treated_car.drive(int(user_command[2]), int(user_command[3]))
        print(result)
    elif user_command[0] == "Refuel":
        treated_car = available_cars[user_command[1]]
        result = treated_car.refuel(int(user_command[2]))
        print(result)
    elif user_command[0] == "Revert":
        treated_car = available_cars[user_command[1]]
        result = treated_car.revert(int(user_command[2]))
        if result != None:
            print(result)

# print(available_cars)

for car in available_cars.values():
    if not car.sold:
        print(car)
