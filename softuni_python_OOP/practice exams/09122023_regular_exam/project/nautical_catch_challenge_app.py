from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = ["FreeDiver", "ScubaDiver"]
    FISH_TYPES = ["PredatoryFish", "DeepSeaFish"]

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.divers:
            for diver in self.divers:
                if diver.name == diver_name:
                    return f"{diver_name} is already a participant."

        diver_object = globals()[diver_type]
        diver = diver_object(diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            rejected_fish_name = next(filter(lambda f: f.name == fish_name, self.fish_list))
            if rejected_fish_name:
                return f"{fish_name} is already permitted."
        except StopIteration:
            fish_object = globals()[fish_type]
            fish = fish_object(fish_name, points)
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def diver_validation(self, diver_name):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
            if diver:
                return True
        except StopIteration:
            return False

    def fish_validation(self, fish_name):
        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
            if fish:
                return True
        except StopIteration:
            return False

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        if not self.diver_validation(diver_name):
            return f"{diver_name} is not registered for the competition."

        if not self.fish_validation(fish_name):
            return f"The {fish_name} is not allowed to be caught in this competition."

        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        fish = next(filter(lambda f: f.name == fish_name, self.fish_list))

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)

            if diver.oxygen_level == 0:
                diver.has_health_issue = True

            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:

            if is_lucky:
                diver.hit(fish)
                diver.has_health_issue = True

                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            else:
                diver.miss(fish.time_to_catch)

                if diver.oxygen_level == 0:
                    diver.has_health_issue = True

                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)

            if diver.oxygen_level == 0:
                diver.has_health_issue = True

            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        diver_count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver_count += 1
                diver.has_health_issue = False
                diver.renew_oxy()

        return f"Divers recovered: {diver_count}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))
        result = "**" + diver.name + " Catch Report**\n"
        result += '\n'.join(fish.fish_details() for fish in diver.catch)
        return result

    def competition_statistics(self):

        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = "**Nautical Catch Challenge Statistics**\n"
        result += '\n'.join(str(diver) for diver in sorted_divers)
        return result
