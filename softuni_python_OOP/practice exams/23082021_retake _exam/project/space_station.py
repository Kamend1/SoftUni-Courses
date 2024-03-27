from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class SpaceStation:
    VALID_ASTRONAUT_TYPES = ["Biologist", "Geodesist", "Meteorologist"]

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self._successful_missions = 0
        self._unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut:
            return f"{name} is already added."

        astr_object = globals()[astronaut_type]
        new_astronaut = astr_object(name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)

        if planet:
            return f"{name} is already added."

        new_planet = Planet(name)
        item_list = items.split(", ")
        for item in item_list:
            new_planet.items.append(item)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)

        mission_astronauts = []
        for astronaut in sorted_astronauts:
            if astronaut.oxygen > 30:
                mission_astronauts.append(astronaut)
            if len(mission_astronauts) == 5:
                break

        if len(mission_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        counter = 0
        for astronaut in mission_astronauts:
            counter += 1
            while True:
                collected_item = planet.items.pop()
                astronaut.backpack.append(collected_item)
                astronaut.breathe()

                if astronaut.oxygen < astronaut.OXYGEN_PER_BREATH:
                    break

                if not planet.items:
                    self._successful_missions += 1
                    return (f"Planet: {planet_name} was explored. "
                            f"{counter} astronauts participated in collecting items.")

        self._unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self._successful_missions} successful missions!"]
        result.append(f"{self._unsuccessful_missions} missions were not completed!")
        result.append("Astronauts' info:")

        for astronaut in self.astronaut_repository.astronauts:
            result.append(str(astronaut))

        return "\n".join(result)
