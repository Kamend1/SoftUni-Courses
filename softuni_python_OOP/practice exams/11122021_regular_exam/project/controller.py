from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars: List[SportsCar: Car, MuscleCar: Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_CAR_TYPES:
            car_object = globals()[car_type]
            new_car = car_object(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):

        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):

        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):

        driver = next(filter(lambda x: x.name == driver_name, self.drivers), None)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = None
        for index in range(len(self.cars) - 1, - 1, -1):
            if self.cars[index].car_type == car_type and not self.cars[index].is_taken:
                car = self.cars[index]
                break

        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            new_model = car.model
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."
        else:
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):

        race = next(filter(lambda r: r.name == race_name, self.races), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(race.drivers, key=lambda d: -d.car.speed_limit)

        result = []
        for index in range(3):
            sorted_drivers[index].number_of_wins += 1
            name = sorted_drivers[index].name
            speed_limit = sorted_drivers[index].car.speed_limit
            result.append(f"Driver {name} wins the {race_name} race with a speed of {speed_limit}.")

        return "\n".join(result)
