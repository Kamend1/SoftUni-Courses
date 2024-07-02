from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUM_TYPES = ["FreshwaterAquarium", "SaltwaterAquarium"]
    VALID_DECORATION_TYPES = ["Ornament", "Plant"]
    VALID_FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self):
        dr = DecorationRepository()
        self.decorations_repository: DecorationRepository = dr
        self.aquariums: List[FreshwaterAquarium: BaseAquarium, SaltwaterAquarium: BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_AQUARIUM_TYPES:
            return "Invalid aquarium type."

        aq_obj = globals()[aquarium_type]
        new_aquarium = aq_obj(aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.VALID_DECORATION_TYPES:
            return "Invalid decoration type."

        de_obj = globals()[decoration_type]
        new_decoration = de_obj()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums), None)

        if aquarium:
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration != "None":
                aquarium.add_decoration(decoration)
                self.decorations_repository.remove(decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."

            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums), None)
        fish_object = globals()[fish_type]
        new_fish = fish_object(fish_name, fish_species, price)
        if aquarium:
            return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums), None)

        if aquarium:
            aquarium.feed()

            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = next(filter(lambda a: a.name == aquarium_name, self.aquariums), None)

        if aquarium:
            value_fish = sum([fish.price for fish in aquarium.fish])
            value_decorations = sum([decoration.price for decoration in aquarium.decorations])
            total_value = value_fish + value_decorations

            return f"The value of Aquarium {aquarium.name} is {total_value:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return "\n".join(result)
