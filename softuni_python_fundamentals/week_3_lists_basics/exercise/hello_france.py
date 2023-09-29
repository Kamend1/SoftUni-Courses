items_list = input().split("|")
budget = int(input())
train_ticket = 150
difference = train_ticket - budget
item_type = []
item_price = []
items_bought = []
profit = 0

for item in items_list:
    item_type.append(item.split('->')[0])
    item_price.append(float(item.split('->')[1]))

for idx in range(len(item_type)):
    if item_type[idx] == "Clothes" and item_price[idx] <= 50:
        if item_price[idx] <= budget:
            budget -= item_price[idx]
            items_bought.append(item_price[idx] * 1.4)
            profit += item_price[idx] * 0.4
    if item_type[idx] == "Shoes" and item_price[idx] <= 35:
        if item_price[idx] <= budget:
            budget -= item_price[idx]
            items_bought.append(item_price[idx] * 1.4)
            profit += item_price[idx] * 0.4
    if item_type[idx] == "Accessories" and item_price[idx] <= 20.50:
        if item_price[idx] <= budget:
            budget -= item_price[idx]
            items_bought.append(item_price[idx] * 1.4)
            profit += item_price[idx] * 0.4


for item in items_bought:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if sum(items_bought) + budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
