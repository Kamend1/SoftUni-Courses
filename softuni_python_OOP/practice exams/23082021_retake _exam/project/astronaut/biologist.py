from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_PER_BREATH = 5
    DEFAULT_INIT_OXYGEN = 70

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_INIT_OXYGEN)

    @property
    def type(self):
        return "Biologist"
