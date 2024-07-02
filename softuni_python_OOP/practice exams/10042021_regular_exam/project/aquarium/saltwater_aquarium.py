from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    VALID_FISH_TYPES = ["SaltwaterFish"]
    DEFAULT_INITIAL_CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_INITIAL_CAPACITY)

    @property
    def type(self):
        return "SaltwaterAquarium"
