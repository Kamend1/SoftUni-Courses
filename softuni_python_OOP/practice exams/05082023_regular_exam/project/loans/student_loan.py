from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    AMOUNT = 2000.0
    INTEREST_RATE = 1.5
    INCREMENTAL_INTEREST = 0.2
    TYPE_ = "StudentLoan"

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREMENTAL_INTEREST
