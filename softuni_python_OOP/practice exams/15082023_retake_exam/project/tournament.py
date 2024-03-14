from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = ['ElbowPad', 'KneePad']
    VALID_TEAM_TYPES = ['IndoorTeam', 'OutdoorTeam']

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[KneePad: BaseEquipment, ElbowPad: BaseEquipment] = []
        self.teams: List[IndoorTeam: BaseTeam, OutdoorTeam: BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")

        equipment_object = globals()[equipment_type]
        equipment = equipment_object()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise ValueError("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team_object = globals()[team_type]
        team = team_object(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        filter_eq_by_type = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type]
        equipment = filter_eq_by_type[-1]
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):

        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        counter = 0

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                equipment.increase_price()
                counter += 1

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1 = next(filter(lambda team: team.name == team_name1, self.teams))
        team_2 = next(filter(lambda team: team.name == team_name2, self.teams))

        if team_1.__class__.__name__ != team_2.__class__.__name__:
            raise Exception(f"Game cannot start! Team types mismatch!")

        team_1_protection = sum([equipment.protection for equipment in team_1.equipment])
        team_2_protection = sum([equipment.protection for equipment in team_2.equipment])

        team_1_result = team_1.advantage + team_1_protection
        team_2_result = team_2.advantage + team_2_protection

        if team_1_result == team_2_result:
            return "No winner in this game."

        if team_1_result > team_2_result:
            team_1.win()
            return f"The winner is {team_1.name}."

        if team_1_result < team_2_result:
            team_2.win()
            return f"The winner is {team_2.name}."

    def get_statistics(self):

        sorted_teams = sorted(self.teams, key=lambda team: -team.wins)

        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

