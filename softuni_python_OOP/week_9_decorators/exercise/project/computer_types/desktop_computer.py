import math
from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    VALID_PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    MAX_RAM = 128
    VALID_RAM = [2 ** i for i in range(1, math.ceil(math.log2(int(MAX_RAM))) + 1)]
    RAM_PRICE_MULTIPLE = 100

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_PROCESSORS.keys():
            raise ValueError(f"{processor} is not compatible with desktop computer "
                             f"{self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAM or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer "
                             f"{self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.VALID_PROCESSORS[processor] + int(self.RAM_PRICE_MULTIPLE * int(math.log2(ram)))
        return f"Created {self.__repr__()} for {round(self.price)}$."
