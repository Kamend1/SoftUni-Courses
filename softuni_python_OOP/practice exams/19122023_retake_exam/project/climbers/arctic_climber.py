from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    EXTREME_FACTOR = 2
    NORMAL_FACTOR = 1.5
    # GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def __init__(self, name: str, strength: float = 200):
        super().__init__(name, strength)
        # self.gear = self.GEAR

    def can_climb(self):
        if self.strength < 100:
            return False

        return True

    def climb(self, peak: BasePeak):
        if self.can_climb():
            if peak.difficulty_level == "Extreme":
                self.strength -= 20 * self.EXTREME_FACTOR
            else:
                self.strength -= 20 * self.NORMAL_FACTOR

            self.conquered_peaks.append(peak.name)
