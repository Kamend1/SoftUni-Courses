from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse: List[DesktopComputer: Computer, Laptop: Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Desktop Computer":
            type_computer = "DesktopComputer"

        computer_object = globals()[type_computer]
        new_computer = computer_object(manufacturer, model)
        self.warehouse.append(new_computer)
        return new_computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
                self.warehouse.remove(comp)
                self.profits += client_budget - comp.price
                return f"{comp} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
