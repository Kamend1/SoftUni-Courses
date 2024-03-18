from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.delicacy import Delicacy


class ChristmasPastryShopApp:
    VALID_DELICACIES = ["Gingerbread", "Stolen"]
    VALID_BOOTHS = ["Open Booth", "Private Booth"]

    def __init__(self):
        self.booths: List[OpenBooth: Booth, PrivateBooth: Booth] = []
        self.delicacies: List[Gingerbread: Delicacy, Stolen: Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        delicacy = next(filter(lambda d: d.name == name, self.delicacies), None)

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy_object = globals()[type_delicacy]
        new_delicacy = delicacy_object(name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths), None)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        type_of_booth, booth = type_booth.split()
        type_object = type_of_booth + booth
        booth_object = globals()[type_object]
        new_booth = booth_object(booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths), None)
        delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies), None)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):

        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths), None)

        bill = booth.calculate_income()
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0.00
        booth.is_reserved = False

        result = "Booth " + str(booth.booth_number) + ":" + "\n" + "Bill: " + f"{bill:.2f}lv."

        return result

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
