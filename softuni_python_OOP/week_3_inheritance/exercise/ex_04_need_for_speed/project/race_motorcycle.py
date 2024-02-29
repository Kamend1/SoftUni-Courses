from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION: float = 8

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)