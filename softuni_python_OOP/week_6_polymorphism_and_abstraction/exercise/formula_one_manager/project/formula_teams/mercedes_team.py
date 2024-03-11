from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    # RACE_EXPENSE = 200000
    # SPONSORS = {'Petronas': {1: 1000000, 3: 500000}, 'TeamViewer': {5: 100000, 7: 50000}}

    @property
    def sponsors(self):
        return {'Petronas': {1: 1000000, 3: 500000}, 'TeamViewer': {5: 100000, 7: 50000}}

    @property
    def race_expense(self):
        return 200000
