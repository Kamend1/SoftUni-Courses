from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    DEFAULT_PORTION = 245

    def __init__(self, name, price):
        super().__init__(name, self.DEFAULT_PORTION, price)
    @property
    def type(self):
        return "Cake"
