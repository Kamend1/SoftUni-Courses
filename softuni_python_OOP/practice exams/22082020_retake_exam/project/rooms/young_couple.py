from project.rooms.room import Room
from typing import List
from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV


class YoungCouple(Room):
    DEFAULT_MEMBERS = 2
    DEFAULT_ROOM_COST = 20
    DEFAULT_APPLIANCE_LIST = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.DEFAULT_MEMBERS)
        self.room_cost = self.DEFAULT_ROOM_COST
        self.appliances: List[Fridge: Appliance, Laptop: Appliance, Stove: Appliance, TV: Appliance] \
            = self.DEFAULT_APPLIANCE_LIST
