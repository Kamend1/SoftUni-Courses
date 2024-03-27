from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    # OXYGEN_PER_BREATH = 10
    DEFAULT_INIT_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_INIT_OXYGEN)

    @property
    def type(self):
        return "Geodesist"
