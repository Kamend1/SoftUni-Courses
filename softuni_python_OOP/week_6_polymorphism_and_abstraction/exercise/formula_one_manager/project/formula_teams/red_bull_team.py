from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    RACE_EXPENSE = 250000
    SPONSORS = {'Oracle': {1: 1500000, 2: 800000}, 'Honda': {8: 20000, 10: 10000}}

    @property
    def sponsors(self):
        return {'Oracle': {1: 1500000, 2: 800000}, 'Honda': {8: 20000, 10: 10000}}

    @property
    def race_expense(self):
        return 250000


