from project.software.software import Software
from math import floor


class ExpressSoftware(Software):
    _TYPE = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self._TYPE, capacity_consumption, floor(memory_consumption * 2))
