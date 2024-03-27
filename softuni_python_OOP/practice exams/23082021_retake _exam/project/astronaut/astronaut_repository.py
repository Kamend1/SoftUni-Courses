from typing import List

from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautRepository:

    def __init__(self):
        self.astronauts: List[Biologist: Astronaut, Geodesist: Astronaut, Meteorologist: Astronaut] = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = next(filter(lambda a: a.name == name, self.astronauts), None)

        return astronaut
