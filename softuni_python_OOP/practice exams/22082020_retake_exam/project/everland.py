from typing import List

from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:

    def __init__(self):
        self.rooms: List[AloneOld: Room,
                    AloneYoung: Room,
                    OldCouple: Room,
                    YoungCouple: Room,
                    YoungCoupleWithChildren: Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0

        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []

        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.budget >= total_cost:
                room.budget -= total_cost
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return "\n".join(result)

    def status(self):
        all_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        result = [f"Total population: {all_people_in_the_hotel}"]
        for room in self.rooms:
            result.append(f"{room.family_name} with "
                          f"{room.members_count} members. "
                          f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for index in range(len(room.children)):
                    result.append(f"--- Child {index + 1} monthly cost: {room.children[index].cost * 30:.2f}$")
            cost_of_all_appliances_for_one_month = sum(appliance.cost for appliance in room.appliances) * 30
            result.append(f"--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$")

        return "\n".join(result)