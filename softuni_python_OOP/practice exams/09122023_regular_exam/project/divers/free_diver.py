from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DEFAULT_OXYGEN_LEVEL = 120
    MISS_OXYGEN_PERCENT = 0.60

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)
