from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, fuel: float, horse_power: int):
        fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        super().__init__(fuel, horse_power)