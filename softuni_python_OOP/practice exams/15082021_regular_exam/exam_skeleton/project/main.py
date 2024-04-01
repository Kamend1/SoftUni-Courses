from project.bakery import Bakery
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

bakery = Bakery("Kamen")


bakery.add_food("Bread", "Tipov", 2.45)
bakery.add_food("Bread", "White", 2.15)
bakery.add_food("Cake", "Bavarian", 5.67)
bakery.add_food("Cake", "Choco", 4.89)
bakery.add_drink("Water", "500 ml", 500, "Baldaran")
bakery.add_drink("Water", "1500 ml", 500, "Bankya")
bakery.add_drink("Tea", "Black", 200, "Lipton")
bakery.add_drink("Tea", "Fruits", 200, "Lipton")
bakery.add_drink("Tea", "Green", 200, "Lipton")
bakery.add_table("InsideTable", 1, 10)
print(bakery.tables_repository)

table = InsideTable(2, 10)
table1 = OutsideTable(51, 10)
print(table, table1)

