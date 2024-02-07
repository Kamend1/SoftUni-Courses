def shopping_list(budget, **kwargs):
    shopping_list_dict = {}
    result = ""
    if budget < 100:
        return "You do not have enough budget."
    else:
        for item, item_data in kwargs.items():
            price, quantity = item_data
            amount = float(price) * int(quantity)
            if amount <= budget:
                shopping_list_dict[item] = shopping_list_dict.get(item, amount)
                result += f"You bought {item} for {amount:.2f} leva.\n"
                budget -= amount

            if len(shopping_list_dict) == 5:
                break

            if budget <= 0:
                break

    return result

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(94.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

