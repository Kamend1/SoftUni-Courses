from typing import List

from project.climbers.base_climber import BaseClimber
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.base_peak import BasePeak
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = ['ArcticClimber', 'SummitClimber']
    VALID_PEAKS = ['ArcticPeak', 'SummitPeak']

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        if self.climbers:
            for climber in self.climbers:
                if climber.name == climber_name:
                    return f"{climber_name} has been already registered."

        climber_object = globals()[climber_type]
        climber = climber_object(climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        peak_object = globals()[peak_type]
        peak = peak_object(peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))

        missing_gear = [item for item in peak.RECOMMENDED_GEAR if item not in gear]

        if missing_gear:
            climber.is_prepared = False
            return (f"{climber_name} is not prepared to climb {peak_name}. "
                    f"Missing gear: {', '.join(sorted(missing_gear))}.")

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers_to_sort = [climber for climber in self.climbers if len(climber.conquered_peaks) > 0]
        sorted_climbers = sorted(climbers_to_sort, key=lambda x: (-len(x.conquered_peaks), x.name))

        conquered_peaks = set()
        for climber in self.climbers:
            for peak in climber.conquered_peaks:
                conquered_peaks.add(peak)

        result = "Total climbed peaks: " + str(len(conquered_peaks)) + "\n**Climber's statistics:**\n" \
                 + '\n'.join(str(climber) for climber in sorted_climbers)

        return result
