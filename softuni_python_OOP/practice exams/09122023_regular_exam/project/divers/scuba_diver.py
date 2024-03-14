from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL = 540
    MISS_OXYGEN_PERCENT = 0.30

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)
