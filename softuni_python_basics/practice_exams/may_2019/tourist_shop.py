from sys import maxsize
tourist_budget = float(input())
budget_left = tourist_budget
amount_spent = 0
number_products = 0

for i in range(1, maxsize):
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {number_products} products for {amount_spent:.2f} leva.")
        break
    if i % 3 == 0:
        product_price = float(input())
        product_price /= 2
        if product_price > budget_left:
            print("You don't have enough money!")
            print(f"You need {product_price - budget_left:.2f} leva!")
            break
        else:
            amount_spent += product_price
            budget_left -= product_price
            number_products += 1
    else:
        product_price = float(input())
        if product_price > budget_left:
            print("You don't have enough money!")
            print(f"You need {product_price - budget_left:.2f} leva!")
            break
        else:
            amount_spent += product_price
            budget_left -= product_price
            number_products += 1
