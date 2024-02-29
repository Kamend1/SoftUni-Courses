from project.car import Car


class FamilyCar(Car):

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)