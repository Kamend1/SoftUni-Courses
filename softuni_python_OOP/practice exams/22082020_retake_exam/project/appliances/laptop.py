from project.appliances.appliance import Appliance


class Laptop(Appliance):
    DEFAULT_COST = 1

    def __init__(self):
        super().__init__(self.DEFAULT_COST)

    @property
    def type(self):
        return "Laptop"
