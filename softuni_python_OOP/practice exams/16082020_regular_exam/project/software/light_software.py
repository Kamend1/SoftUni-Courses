from project.software.software import Software
from math import floor


class LightSoftware(Software):
    _TYPE = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self._TYPE, floor(1.5 * capacity_consumption), floor(memory_consumption /2))
