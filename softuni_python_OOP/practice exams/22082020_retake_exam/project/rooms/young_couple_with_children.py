from project.people.child import Child
from project.rooms.room import Room
from typing import List
from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV


class YoungCoupleWithChildren(Room):
    DEFAULT_MEMBERS = 2
    DEFAULT_ROOM_COST = 30
    # DEFAULT_APPLIANCE_LIST = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        num_members = self.DEFAULT_MEMBERS + len(list(children))
        super().__init__(family_name, salary_one + salary_two, num_members)
        self.room_cost = self.DEFAULT_ROOM_COST
        self.children: List[Child] = list(children)
        self.appliances: List[Fridge: Appliance, Laptop: Appliance, Stove: Appliance, TV: Appliance] \
            = [TV() for _ in range(num_members)] \
            + [Fridge() for _ in range(num_members)] \
            + [Laptop() for _ in range(num_members)]
        self.expenses = self.calculate_expenses(self.children, self.appliances)

