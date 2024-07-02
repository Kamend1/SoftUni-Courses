import math
from project.computer_types.computer import Computer


class Laptop(Computer):
    VALID_PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    MAX_RAM = 64
    VALID_RAM = [2 ** i for i in range(1, math.ceil(math.log2(int(MAX_RAM))) + 1)]
    RAM_PRICE_MULTIPLE = 100

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_PROCESSORS.keys():
            raise ValueError(f"{processor} is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAM or ram > self.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.VALID_PROCESSORS[processor] + int(self.RAM_PRICE_MULTIPLE * int(math.log2(ram)))
        return f"Created {self.__repr__()} for {round(self.price)}$."
