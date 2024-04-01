from typing import List

from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if software.capacity_consumption > self._check_available_capacity() \
                or software.memory_consumption > self._check_available_memory():
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def _check_available_memory(self):
        return self.memory - sum(software.memory_consumption for software in self.software_components)

    def _check_available_capacity(self):
        return self.capacity - sum(software.capacity_consumption for software in self.software_components)
