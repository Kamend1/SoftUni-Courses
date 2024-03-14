from project.clients.base_client import BaseClient


class Student(BaseClient):
    INITIAL_INTEREST = 2.0
    CLIENT_INCREMENTAL_INTEREST = 1.0
    TYPE_ = 'Student'
    VALID_LOAN_TYPES = ['StudentLoan']

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INITIAL_INTEREST)


    def increase_clients_interest(self):
        self.interest += self.CLIENT_INCREMENTAL_INTEREST
