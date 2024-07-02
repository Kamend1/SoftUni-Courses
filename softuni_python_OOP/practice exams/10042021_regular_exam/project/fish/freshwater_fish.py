from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE_INCREMENT_EAT = 3
    DEFAULT_INIT_SIZE = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_INIT_SIZE, price)

    @property
    def type(self):
        return "FreshwaterFish"
