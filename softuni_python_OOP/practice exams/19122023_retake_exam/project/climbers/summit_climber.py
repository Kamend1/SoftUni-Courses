from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    EXTREME_FACTOR = 2.5
    NORMAL_FACTOR = 1.3
    # GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def __init__(self, name: str, strength: float = 150):
        super().__init__(name, strength)
        # self.gear = self.GEAR

    def can_climb(self):
        if self.strength < 75:
            return False

        return True

    def climb(self, peak: BasePeak):
        if self.can_climb():
            if peak.difficulty_level != "Advanced":
                self.strength -= 30 * self.EXTREME_FACTOR
            else:
                self.strength -= 30 * self.NORMAL_FACTOR

            self.conquered_peaks.append(peak.name)
