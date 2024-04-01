from project.drink.drink import Drink


class Tea(Drink):
    DEFAULT_PRICE = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.DEFAULT_PRICE, brand)

    @property
    def type(self):
        return "Tea"
