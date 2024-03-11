from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam

class NotAllTeamsRegistered(Exception):
    pass

class F1SeasonApp:
    VALID_TEAM_NAMES = ["Red Bull", "Mercedes"]

    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.VALID_TEAM_NAMES:
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            red_bull_team = RedBullTeam(budget)
            self.red_bull_team = red_bull_team
        else:
            mercedes_team = MercedesTeam(budget)
            self.mercedes_team = mercedes_team

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.mercedes_team or not self.red_bull_team:
            raise NotAllTeamsRegistered("Not all teams have registered for the season.")

        message_red_bull = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        message_mercedes = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        win_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return (f"Red Bull: {message_red_bull}. Mercedes: {message_mercedes}. "
                f"{win_team} is ahead at the {race_name} race.")