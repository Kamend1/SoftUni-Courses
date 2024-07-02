from project.appliances.appliance import Appliance


class Stove(Appliance):
    DEFAULT_COST = 0.7

    def __init__(self):
        super().__init__(self.DEFAULT_COST)

    @property
    def type(self):
        return "Stove"
