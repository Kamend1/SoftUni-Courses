from typing import List

from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    DEFAULT_MEMBERS = 1
    DEFAULT_ROOM_COST = 10
    DEFAULT_APPLIANCE_LIST = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.DEFAULT_MEMBERS)
        self.room_cost = self.DEFAULT_ROOM_COST
        self.appliances: List[Fridge: Appliance, Laptop: Appliance, Stove: Appliance, TV: Appliance] \
            = self.DEFAULT_APPLIANCE_LIST
