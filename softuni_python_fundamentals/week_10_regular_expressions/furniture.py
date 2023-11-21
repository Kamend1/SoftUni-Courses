import re

user_command = input()
total_money_spend = 0
bought_furniture = []

while user_command != "Purchase":
    pattern = r">>([A-Za-z_-]+)<<(\d+\.?\d+)\!(\d+)"
    matches = re.search(pattern, user_command)

    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_money_spend += float(price) * int(quantity)
    user_command = input()

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_money_spend:.2f}")
