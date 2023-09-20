import sys

beginning_qty_eggs = int(input())
qty_eggs_left = beginning_qty_eggs
qty_eggs_sold = 0

for i in range(sys.maxsize):
    order_type = input()
    if order_type == "Close":
        print("Store is closed!")
        print(f"{qty_eggs_sold} eggs sold.")
        break
    if order_type == "Buy":
        qty_order = int(input())
        if qty_order > qty_eggs_left:
            print("Not enough eggs in store!")
            print(f"You can buy only {qty_eggs_left}.")
            break
        else:
            qty_eggs_left -= qty_order
            qty_eggs_sold += qty_order
    elif order_type == "Fill":
        qty_order = int(input())
        qty_eggs_left += qty_order
