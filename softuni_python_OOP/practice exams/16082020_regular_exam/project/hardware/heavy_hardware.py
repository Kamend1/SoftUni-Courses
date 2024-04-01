from project.hardware.hardware import Hardware
from math import floor


class HeavyHardware(Hardware):
    _TYPE = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self._TYPE, floor(capacity * 2), floor(0.75 * memory))
