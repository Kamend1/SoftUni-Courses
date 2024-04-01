from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = next(filter(lambda h: h.name == hardware_name, System._hardware), None)

        if not hardware:
            return "Hardware does not exist"

        es = ExpressSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(es)
        System._software.append(es)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = next(filter(lambda h: h.name == hardware_name, System._hardware), None)

        if not hardware:
            return "Hardware does not exist"

        ls = LightSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(ls)
        System._software.append(ls)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = next(filter(lambda h: h.name == hardware_name, System._hardware), None)
        software = next(filter(lambda s: s.name == software_name, System._software), None)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_all_reg_soft = sum(software.memory_consumption for software in System._software)
        total_memory_all_reg_hard = sum(hardware.memory for hardware in System._hardware)
        total_capacity_all_reg_soft = sum(software.capacity_consumption for software in System._software)
        total_capacity_all_reg_hard = sum(hardware.capacity for hardware in System._hardware)
        result = [f"System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {total_memory_all_reg_soft} / "
                  f"{total_memory_all_reg_hard}",
                  f"Total Capacity Taken: {total_capacity_all_reg_soft} / "
                  f"{total_capacity_all_reg_hard}"
                  ]

        return "\n".join(result)

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.append(f"Hardware Component - {hardware.name}")
            number_express = len([software for software in hardware.software_components if software._TYPE == "Express"])
            result.append(f"Express Software Components: {number_express}")
            number_light = len([software for software in hardware.software_components if software._TYPE == "Light"])
            result.append(f"Light Software Components: {number_light}")
            memory_installed = sum(software.memory_consumption for software in hardware.software_components)
            result.append(f"Memory Usage: {memory_installed} / {hardware.memory}")
            capacity_installed = sum(software.capacity_consumption for software in hardware.software_components)
            result.append(f"Capacity Usage: {capacity_installed} / {hardware.capacity}")
            result.append(f"Type: {hardware._TYPE}")
            if hardware.software_components:
                result.append(f"Software Components: {', '.join(software.name for software in hardware.software_components)}")
            else:
                result.append(f"Software Components: None")

        return "\n".join(result)
