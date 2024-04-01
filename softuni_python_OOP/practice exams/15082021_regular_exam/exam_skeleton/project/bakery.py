from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    VALID_FOOD_TYPES = ["Bread", "Cake"]
    VALID_DRINK_TYPES = ["Tea", "Water"]
    VALID_TABLE_TYPES = ["InsideTable", "OutsideTable"]

    def __init__(self, name):
        self.name = name
        self.food_menu: List[Bread: BakedFood, Cake: BakedFood] = []
        self.drinks_menu: List[Tea: Drink, Water: Drink] = []
        self.tables_repository: List[InsideTable: Table, OutsideTable: Table] = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        food = next(filter(lambda f: f.name == name, self.food_menu), None)

        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.VALID_FOOD_TYPES:
            food_object = globals()[food_type]
            new_food = food_object(name, price)
            self.food_menu.append(new_food)
            return f"Added {new_food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = next(filter(lambda d: d.name == name, self.drinks_menu), None)

        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.VALID_DRINK_TYPES:
            drink_object = globals()[drink_type]
            new_drink = drink_object(name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {new_drink.name} ({new_drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = next(filter(lambda t: t.table_number == table_number, self.tables_repository), None)

        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        # new_table = None
        # if table_type in self.VALID_TABLE_TYPES:
        #     table_object = globals()[table_type]
        #     try:
        #         new_table = table_object(table_number, capacity)
        #     except ValueError:
        #         pass
        table_object = globals()[table_type]
        new_table = table_object(table_number, capacity)

        if new_table:
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *foods):
        table = next(filter(lambda t: t.table_number == table_number, self.tables_repository), None)

        if not table:
            return f"Could not find table {table_number}"

        ordered_foods = []
        unavailable_foods = []
        for food in foods:
            ord_food = next(filter(lambda f: f.name == food, self.food_menu), None)
            if ord_food:
                table.order_food(ord_food)
                ordered_foods.append(str(ord_food))
            else:
                unavailable_foods.append(food)

        result = [f"Table {table_number} ordered:"]
        result.extend(ordered_foods)
        result.append(f"{self.name} does not have in the menu:")
        result.extend(unavailable_foods)

        return "\n".join(result)

    def order_drink(self, table_number: int, *drinks):
        table = next(filter(lambda t: t.table_number == table_number, self.tables_repository), None)

        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = []
        unavailable_drinks = []
        for drink in drinks:
            ord_drink = next(filter(lambda d: d.name == drink, self.drinks_menu), None)
            if ord_drink:
                table.order_drink(ord_drink)
                ordered_drinks.append(str(ord_drink))
            else:
                unavailable_drinks.append(drink)

        result = [f"Table {table_number} ordered:"]
        result.extend(ordered_drinks)
        result.append(f"{self.name} does not have in the menu:")
        result.extend(unavailable_drinks)

        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = next(filter(lambda t: t.table_number == table_number, self.tables_repository), None)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()

        result = [f"Table: {table_number}", f"Bill: {table_bill:.2f}"]
        return "\n".join(result)

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())

        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
