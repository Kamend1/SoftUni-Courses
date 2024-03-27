from typing import List

from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets: List = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        planet = next(filter(lambda p: p.name == name, self.planets), None)

        return planet
