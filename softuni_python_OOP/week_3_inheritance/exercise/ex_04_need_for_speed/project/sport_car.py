from project.car import Car



class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION: float = 10

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)