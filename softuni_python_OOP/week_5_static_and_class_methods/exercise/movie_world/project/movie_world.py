from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        capacity = self.customer_capacity()
        if len(self.customers) < capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        capacity = self.dvd_capacity()
        if len(self.dvds) < capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return

        try:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return

        if customer and dvd:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

            if dvd.is_rented:
                return "DVD is already rented"

            if customer.age < dvd.age_restriction:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return

        try:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""

        customers = '\n'.join(str(customer) for customer in self.customers)
        dvds = '\n'.join(str(dvd) for dvd in self.dvds)

        result += customers
        result += "\n" + dvds

        return result
