budget = float(input())
category_ticket = str(input())
number_people = int(input())
transport_cost = 0
price_VIP = 499.99
price_normal = 249.99

if number_people >= 50:
    transport_cost = budget * 0.25
elif 25 <= number_people <= 49:
    transport_cost = budget * 0.40
elif 10 <= number_people <= 24:
    transport_cost = budget * 0.50
elif 5 <= number_people <= 9:
    transport_cost = budget * 0.60
else:
    transport_cost = budget * 0.75

amount_spent = 0

if category_ticket == "VIP":
    amount_spent = number_people * price_VIP + transport_cost
else:
    amount_spent = number_people * price_normal + transport_cost

difference = abs(amount_spent - budget)

if amount_spent <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
