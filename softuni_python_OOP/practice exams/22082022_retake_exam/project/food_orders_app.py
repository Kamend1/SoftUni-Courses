from project.client import Client
from typing import List
from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEAL_TYPES = ["Starter", "MainDish", "Dessert"]
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: List[Dessert: Meal, MainDish: Meal, Starter: Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)

        if client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {new_client.phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEAL_TYPES:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = [meal.details() for meal in self.menu]

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list), None)
        if not client:
            self.register_client(client_phone_number)
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        ordered_food = {}

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu), None)
            if meal:
                if meal.quantity >= quantity:
                    ordered_food[meal.name] = ordered_food.get(meal_name, 0) + quantity
                else:
                    ordered_food = {}
                    raise Exception(f"Not enough quantity of {meal.TYPE_}: {meal_name}!")
            else:
                ordered_food = {}
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, quantity in ordered_food.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu))
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity
            meal.quantity -= quantity
            client.ordered_food[meal.name] = client.ordered_food.get(meal_name, 0) + quantity

        return (f"Client {client_phone_number} successfully ordered "
                f"{', '.join(meal.name for meal in client.shopping_cart)} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client.ordered_food.items():
            meal = next(filter(lambda m: m.name == meal_name, self.menu))
            meal.quantity += quantity

        client.bill = 0.00
        client.shopping_cart = []
        client.ordered_food = {}

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        bill = client.bill
        client.shopping_cart = []
        client.ordered_food = {}

        client.bill = 0.00
        self.RECEIPT_ID += 1
        return (f"Receipt #{self.RECEIPT_ID} with total amount of "
                f"{bill:.2f} was successfully paid for {client.phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
