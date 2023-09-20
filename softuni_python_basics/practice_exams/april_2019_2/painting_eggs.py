size_eggs = input()
color_eggs = input()
number_lots = int(input())
price = 0

if size_eggs == "Large":
    if color_eggs == "Red":
        price = 16
    elif color_eggs == "Green":
        price = 12
    elif color_eggs == "Yellow":
        price = 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        price = 13
    elif color_eggs == "Green":
        price = 9
    elif color_eggs == "Yellow":
        price = 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        price = 9
    elif color_eggs == "Green":
        price = 8
    elif color_eggs == "Yellow":
        price = 5

total_income = price * number_lots * 0.65

print(f"{total_income:.2f} leva.")
