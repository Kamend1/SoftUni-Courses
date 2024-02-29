from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = Motorcycle.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)
