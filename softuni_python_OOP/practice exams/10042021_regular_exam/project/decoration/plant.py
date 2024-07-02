from project.decoration.base_decoration import BaseDecoration

class Plant(BaseDecoration):
    DEFAULT_COMFORT = 5
    DEFAULT_PRICE = 10

    def __init__(self):
        super().__init__(self.DEFAULT_COMFORT, self.DEFAULT_PRICE)

    @property
    def type(self):
        return "Plant"
