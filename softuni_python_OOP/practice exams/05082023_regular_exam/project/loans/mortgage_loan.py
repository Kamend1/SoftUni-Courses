from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    AMOUNT = 50000.0
    INTEREST_RATE = 3.5
    INCREMENTAL_INTEREST = 0.5
    TYPE_ = "MortgageLoan"

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREMENTAL_INTEREST
