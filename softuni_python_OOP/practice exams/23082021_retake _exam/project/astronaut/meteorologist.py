from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_PER_BREATH = 15
    DEFAULT_INIT_OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_INIT_OXYGEN)

    @property
    def type(self):
        return "Meteorologist"
