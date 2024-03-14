from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    VALID_LOAN_TYPES = ["StudentLoan", "MortgageLoan"]
    VALID_CLIENT_TYPES = ["Student", "Adult"]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.clients: List[Student: BaseClient, Adult: BaseClient] = []
        self.loans: List[StudentLoan: BaseLoan, MortgageLoan: BaseLoan] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan_object = globals()[loan_type]
        loan = loan_object()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return f"Not enough bank capacity."

        client_object = globals()[client_type]
        client = client_object(client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next(filter(lambda l: l.TYPE_ == loan_type, self.loans))
        client = next(filter(lambda c: c.client_id == client_id, self.clients))

        if loan.TYPE_ not in client.VALID_LOAN_TYPES:
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0

        for loan in self.loans:
            if loan.TYPE_ == loan_type:
                loan.increase_interest_rate()
                counter += 1

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1

        return f"Number of clients affected: {counter}."

    def get_statistics(self):

        granted_loans = sum([len(client.loans) for client in self.clients])
        granted_sum = sum((sum(loan.amount for loan in client.loans) for client in self.clients))
        avg_client_interest_rate = sum(client.interest for client in self.clients) / len(self.clients) \
            if self.clients else 0

        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum([client.income for client in self.clients]):.2f}",
                  f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}",
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
                  ]

        return "\n".join(result)
