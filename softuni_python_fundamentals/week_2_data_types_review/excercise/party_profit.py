group_size = int(input())
days = int(input())
profit = 0

current_day = 1

while current_day <= days:
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
        profit -= 2 * group_size
    profit += 50
    profit -= 2 * group_size
    if current_day % 3 == 0:
        profit -= group_size * 3
    if current_day % 5 == 0:
        profit += 20 * group_size

    current_day += 1

profit_companion = profit // group_size

print(f"{group_size} companions received {profit_companion} coins each.")
