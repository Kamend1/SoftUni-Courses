from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    VALID_FISH_TYPES = ["FreshwaterFish"]
    DEFAULT_INITIAL_CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_INITIAL_CAPACITY)

    @property
    def type(self):
        return "FreshwaterAquarium"
