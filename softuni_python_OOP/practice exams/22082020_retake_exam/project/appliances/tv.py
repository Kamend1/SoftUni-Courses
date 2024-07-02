from project.appliances.appliance import Appliance


class TV(Appliance):
    DEFAULT_COST = 1.5

    def __init__(self):
        super().__init__(self.DEFAULT_COST)

    @property
    def type(self):
        return "TV"
