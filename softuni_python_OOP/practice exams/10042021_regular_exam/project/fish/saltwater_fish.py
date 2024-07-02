from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE_INCREMENT_EAT = 2
    DEFAULT_INIT_SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.DEFAULT_INIT_SIZE, price)

    @property
    def type(self):
        return "SaltwaterFish"
